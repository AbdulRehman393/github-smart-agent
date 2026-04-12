import os
from langchain_core.documents import Document
from src.config import ALLOWED_EXTENSIONS

def read_repo_documents(repo_path: str) -> list[Document]:
    docs = []

    for root, dirs, files in os.walk(repo_path):
        # skip junk folders
        dirs[:] = [
            d for d in dirs 
            if d not in {".git", "node_modules", "dist", "build", "__pycache__", ".venv", "venv"}
        ]

        for file in files:
            ext = os.path.splitext(file)[1].lower()
            if ext not in ALLOWED_EXTENSIONS:
                continue

            full_path = os.path.join(root, file)
            rel_path = os.path.relpath(full_path, repo_path)

            try:
                with open(full_path, "r", encoding="utf-8", errors="ignore") as f:
                    content = f.read()

                if content.strip():
                    docs.append(
                        Document(
                            page_content=content,
                            metadata={"path": rel_path, "source": full_path, "ext": ext}
                        )
                    )
            except Exception:
                continue

    return docs