import os
from langchain_openai import ChatOpenAI
from src.config import OPENROUTER_API_KEY, OPENROUTER_BASE_URL, OPENROUTER_MODEL

SYSTEM_PROMPT = """
You are a senior code auditor.
Analyze the given source code and list:

1. Bugs
2. Weaknesses
3. Security issues
4. Risk level
5. Exact file + line involved
6. Suggested fix

Respond in structured bullet format.
"""

def run_bug_detection(repo_path: str) -> dict:
    """
    Scan each file using LLM for bugs.
    """

    llm = ChatOpenAI(
        model=OPENROUTER_MODEL,
        api_key=OPENROUTER_API_KEY,
        base_url=OPENROUTER_BASE_URL,
        default_headers={
            "HTTP-Referer": "http://localhost",
            "X-Title": "GitHub Smart Agent"
        },
        temperature=0
    )

    report = {}

    for root, _, files in os.walk(repo_path):
        for f in files:
            if not f.endswith((".py", ".js", ".ts")):
                continue

            path = os.path.join(root, f)
            try:
                with open(path, "r", encoding="utf-8", errors="ignore") as fp:
                    content = fp.read()

                result = llm.invoke(
                    f"{SYSTEM_PROMPT}\n\nFile: {path}\n\n{content}"
                )

                report[path] = result.content

            except Exception as e:
                report[path] = f"Error analyzing file: {str(e)}"

    return report