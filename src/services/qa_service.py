from langchain_openai import ChatOpenAI
from langchain.chains import RetrievalQA
from src.config import OPENROUTER_API_KEY, OPENROUTER_BASE_URL, OPENROUTER_MODEL
from src.rag.retriever import get_retriever


def build_qa_chain(index_path: str):
    retriever = get_retriever(index_path, k=6)

    llm = ChatOpenAI(
        model=OPENROUTER_MODEL,
        api_key=OPENROUTER_API_KEY,
        base_url=OPENROUTER_BASE_URL,
        default_headers={
            "HTTP-Referer": "http://localhost",
            "X-Title": "GitHub Smart Agent"
        },
        temperature=0,
        max_tokens=500   #  FIX: prevents 402 credit errors
    )

    chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        chain_type="stuff",
        return_source_documents=True
    )
    return chain