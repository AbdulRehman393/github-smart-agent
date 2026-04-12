from langchain_openai import ChatOpenAI
from langchain_core.tools import tool
from langchain_community.utilities import SerpAPIWrapper
from chroma_utils import vectorstore
from dotenv import load_dotenv
import os
import re

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '..', '.env'))

retriever = vectorstore.as_retriever(search_kwargs={"k": 2})

@tool
def document_search(q: str):
    """Searches your uploaded documents and returns relevant content."""
    docs = retriever.invoke(q)
    return "\n\n".join([doc.page_content for doc in docs if doc.page_content])

@tool
def web_search(q: str):
    """Live search for current events, weather, or today's date."""
    print(f"web_search called with: {q}")
    wrapper = SerpAPIWrapper()
    result = wrapper.run(q)

    # Ensure result is a string (SerpAPIWrapper can return non-string in some setups)
    if not isinstance(result, str):
        result = str(result)

    # Prevent huge tool output from breaking/overloading the LLM prompt
    return result[:4000]

# Greeting matching (whole message)
GREETINGS = {
    "hi", "hello", "hey", "salaam", "assalam", "assalam o alaikum",
    "good morning", "good afternoon", "good evening"
}

def is_greeting(msg: str) -> bool:
    norm = re.sub(r"[^a-z\s]", "", msg.lower()).strip()
    return norm in GREETINGS

# Keywords that should use web search (live/current)
LIVE_KEYWORDS = [
    "date", "weather", "today", "now", "current", "temperature",
    "recent", "recently", "latest", "update", "updates", "breaking", "news",
    "conflict", "war", "attack", "airstrike", "strike", "missile",
    "killed", "killing", "died", "dead", "death", "martyred", "martyr",
]

def _history_to_text(chat_history) -> str:
    """Converts DB chat_history into a readable text block for the LLM."""
    if not chat_history:
        return ""

    # If already list[dict] with role/content
    if isinstance(chat_history, list) and chat_history and isinstance(chat_history[0], dict):
        lines = []
        for m in chat_history[-8:]:
            role = m.get("role", "user")
            content = m.get("content", "")
            if content:
                lines.append(f"{role}: {content}")
        return "\n".join(lines)

    # Otherwise stringify safely
    try:
        return "\n".join([str(x) for x in chat_history[-8:]])
    except Exception:
        return str(chat_history)

def get_rag_chain(model="nvidia/nemotron-nano-9b-v2:free"):
    llm = ChatOpenAI(
        model=model,
        openai_api_key=os.getenv("OPENROUTER_API_KEY"),
        openai_api_base="https://openrouter.ai/api/v1",
        request_timeout=120
    )

    class AgentRAGChain:
        def invoke(self, inputs):
            user_q = inputs["input"]
            normalized_q = user_q.lower().strip()

            chat_history = inputs.get("chat_history", [])
            history_text = _history_to_text(chat_history)

            print("User asked:", user_q)

            # 1) Greeting
            if is_greeting(normalized_q) or normalized_q in ["how are you?", "what's up?", "are you there?"]:
                return {"answer": "Hello! How can I assist you today?", "source": "greeting"}

            # 2) Documents first (RAG)
            print("Trying PDF/doc search...")
            try:
                doc_answer = document_search(user_q)
            except Exception as e:
                print("document_search failed:", e)
                doc_answer = ""

            print("Doc search result:", (doc_answer[:1200] + "...") if doc_answer else "(empty)")

            if doc_answer and doc_answer.strip():
                check_prompt = (
                    "You are a helpful document assistant. Answer ONLY using the document extract.\n"
                    "Use chat history only to resolve references (he/it/that), but do NOT invent facts.\n"
                    f"Chat history:\n{history_text}\n\n"
                    "If the answer is not present in the document extract, reply ONLY with: NOT FOUND.\n\n"
                    f"Document Extract:\n'''\n{doc_answer}\n'''\n\n"
                    f"User question: {user_q}\n"
                )
                try:
                    llm_result = llm.invoke(check_prompt)
                    content = getattr(llm_result, "content", None) or str(llm_result)
                    print("Doc LLM result:", content)
                    if "NOT FOUND" not in content.upper():
                        return {"answer": content.strip(), "source": "document"}
                except Exception as e:
                    print(f"PDF LLM check failed: {e}")

            # 3) Live/current → web search
            if any(kw in normalized_q for kw in LIVE_KEYWORDS):
                try:
                    tool_data = web_search(user_q)
                except Exception as e:
                    print("web_search failed:", e)
                    return {"answer": f"Sorry, web search failed: {e}", "source": "web"}

                tool_data = (tool_data or "")[:4000]

                web_prompt = (
                    "You are a helpful assistant.\n"
                    "Use the chat history to understand follow-up questions.\n"
                    f"Chat history:\n{history_text}\n\n"
                    f"User question: {user_q}\n\n"
                    "Web results (may be noisy):\n"
                    f"{tool_data}\n\n"
                    "Task:\n"
                    "- Provide a short, direct answer.\n"
                    "- If user asks a follow-up like 'tell me in celsius', use the previous temperature from chat history.\n"
                    "- If results are contradictory or not clearly verified, say you cannot confirm.\n"
                )
                try:
                    llm_result = llm.invoke(web_prompt)
                    content = getattr(llm_result, "content", None) or str(llm_result)
                    return {"answer": content.strip(), "source": "web"}
                except Exception as e:
                    print(f"Web LLM error: {e}")
                    # IMPORTANT: don't dump raw tool data to the user
                    return {
                        "answer": "I found web results but couldn't summarize them right now. Please try again.",
                        "source": "web"
                    }

            # 4) General LLM fallback (conversational)
            print("Trying direct LLM fallback...")
            fallback_prompt = (
                "You are a helpful assistant.\n"
                "Use chat history to answer follow-up questions.\n"
                f"Chat history:\n{history_text}\n\n"
                f"User question: {user_q}\n"
            )
            try:
                result = llm.invoke(fallback_prompt)
                content = getattr(result, "content", None) or str(result)
                print("Direct LLM result:", content)
                return {"answer": content.strip(), "source": "llm"}
            except Exception as e:
                print(f"Agent fallback error: {e}")
                return {"answer": f"Sorry, something went wrong: {e}", "source": "llm"}

    return AgentRAGChain()