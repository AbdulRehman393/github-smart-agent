
from src.services.qa_service import build_qa_chain
from src.services.analysis_service import analyze_repository

class GitHubSmartAgent:
    def __init__(self, index_path: str, repo_path: str):
        self.qa_chain = build_qa_chain(index_path)
        self.repo_path = repo_path

    def ask(self, query: str):
        return self.qa_chain.invoke({"query": query})

    def analyze(self):
        return analyze_repository(self.repo_path)
