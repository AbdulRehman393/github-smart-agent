import subprocess
import os

def run_static_analysis(repo_path: str) -> dict:
    """
    Runs simple static analysis using pylint.
    """

    results = {}

    try:
        process = subprocess.run(
            ["pylint", repo_path],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        results["pylint_output"] = process.stdout

    except Exception as e:
        results["error"] = str(e)

    return results