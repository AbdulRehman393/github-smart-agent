import os
from src.analyzers.static_runner import run_static_analysis
from src.config import ALLOWED_EXTENSIONS
from langchain_openai import ChatOpenAI
from src.config import OPENROUTER_API_KEY, OPENROUTER_BASE_URL, OPENROUTER_MODEL


def get_source_files(repo_path: str, max_files=20):
    """
    Find important source files, skip huge files, and limit count.
    """
    selected = []

    for root, dirs, files in os.walk(repo_path):
        dirs[:] = [d for d in dirs if d not in (
            "node_modules", "dist", "build", "out", "venv",
            ".venv", "__pycache__", ".git", "coverage", "migrations"
        )]

        for file in files:
            if len(selected) >= max_files:
                return selected

            ext = os.path.splitext(file)[1].lower()
            if ext not in ALLOWED_EXTENSIONS:
                continue

            full_path = os.path.join(root, file)

            # Skip huge files
            if os.path.getsize(full_path) > 200_000:  # 200 KB
                continue

            selected.append(full_path)

    return selected


def analyze_repository(repo_path: str):
    """
    Run static analysis + per-file AI bug detection + per-file optimization.
    This avoids token overflow and works for all repo sizes.
    """

    # 1. Static (non-AI)
    static_report = run_static_analysis(repo_path)

    # 2. Collect source files
    files = get_source_files(repo_path, max_files=10)

    if not files:
        return {
            "static_analysis": static_report,
            "bug_detection": "No valid files found.",
            "optimization": "No valid files found."
        }

    # 3. Initialize LLM (use Gemini Flash or DeepSeek)
    llm = ChatOpenAI(
        model=OPENROUTER_MODEL,
        api_key=OPENROUTER_API_KEY,
        base_url=OPENROUTER_BASE_URL,
        temperature=0,
        default_headers={
            "HTTP-Referer": "http://localhost",
            "X-Title": "GitHubSmartAgent"
        }
    )

    bug_results = {}
    opt_results = {}

    # 4. Analyze each file separately
    for file_path in files:
        try:
            with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                content = f.read()
        except:
            continue

        # Skip empty
        if len(content.strip()) < 10:
            continue

        # --- AI Bug Detection ---
        bug_prompt = f"""
You are a senior code auditor.

Analyze ONLY THIS file for:
- bugs
- vulnerabilities
- insecure logic
- risky patterns

Respond in plain text, keep it short.

FILE: {file_path}
CODE:
{content}
"""

        bug_results[file_path] = llm.invoke(
            bug_prompt, max_tokens=500
        ).content

        # --- AI Optimization ---
        opt_prompt = f"""
You are an expert software engineer.

Suggest improvements for:
- performance
- readability
- simplification
- removing dead code

Respond in plain text.

FILE: {file_path}
CODE:
{content}
"""

        opt_results[file_path] = llm.invoke(
            opt_prompt, max_tokens=500
        ).content

    return {
        "static_analysis": static_report,
        "bug_detection": bug_results,
        "optimization": opt_results
    }