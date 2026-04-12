import os
from langchain_openai import ChatOpenAI
from src.config import OPENROUTER_API_KEY, OPENROUTER_BASE_URL, OPENROUTER_MODEL

OPTIMIZE_PROMPT = """
You are a code optimization assistant.
Analyze the code and provide:

1. Performance improvements
2. Readability improvements
3. Memory usage improvements
4. Dead code detection
5. Cleaner refactored version of the code

Give improvements in bullet points + rewrite improved version.
"""

def run_code_optimization(repo_path: str) -> dict:
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
            if not f.endswith(".py"):
                continue

            path = os.path.join(root, f)
            try:
                with open(path, "r", encoding="utf-8", errors="ignore") as fp:
                    content = fp.read()

                result = llm.invoke(
                    f"{OPTIMIZE_PROMPT}\n\nFile: {path}\n\n{content}"
                )

                report[path] = result.content

            except Exception as e:
                report[path] = f"Error: {str(e)}"

    return report