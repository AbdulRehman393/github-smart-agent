import os
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
from src.rag.embeddings import get_embeddings

def index_repo(chunks: list[Document], index_path: str):
    os.makedirs(index_path, exist_ok=True)

    embeddings = get_embeddings()
    db = FAISS.from_documents(chunks, embeddings)

    db.save_local(index_path)

def load_repo_index(index_path: str):
    embeddings = get_embeddings()
    return FAISS.load_local(
        index_path,
        embeddings,
        allow_dangerous_deserialization=True
    )