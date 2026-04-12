from src.rag.vector_store import load_repo_index

def get_retriever(index_path: str, k: int = 6):
    db = load_repo_index(index_path)
    return db.as_retriever(search_kwargs={"k": k})