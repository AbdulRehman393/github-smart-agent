import os
from src.config import REPOS_DIR, INDEX_DIR
from src.github_loader.repo_cloner import clone_repo, repo_name_from_url
from src.github_loader.repo_parser import read_repo_documents
from src.rag.chunker import chunk_documents
from src.rag.vector_store import index_repo
import shutil

def ingest_repository(repo_url: str, branch: str | None = None) -> dict:
    repo_path = clone_repo(repo_url, REPOS_DIR, branch)
    repo_name = repo_name_from_url(repo_url)
    index_path = os.path.join(INDEX_DIR, repo_name)

    docs = read_repo_documents(repo_path)
    chunks = chunk_documents(docs)

    # ✅ ADD THIS: remove old FAISS index if it already exists
    if os.path.exists(index_path):
        shutil.rmtree(index_path)

    # Build new FAISS index
    index_repo(chunks, index_path)

    return {
        "repo_name": repo_name,
        "repo_path": repo_path,
        "index_path": index_path,
        "documents": len(docs),
        "chunks": len(chunks),
    }