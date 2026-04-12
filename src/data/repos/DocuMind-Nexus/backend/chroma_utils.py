from langchain_community.document_loaders import PyPDFLoader, Docx2txtLoader, UnstructuredHTMLLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from typing import List
from langchain_core.documents import Document
from langchain_core.embeddings import Embeddings
import hashlib
import os
from dotenv import load_dotenv

# Load the API key from .env file
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '..', '.env'))

# Initialize text splitter
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200,
    length_function=len
)


class SimpleHashEmbeddings(Embeddings):
    """Simple hash-based embeddings that work 100% offline.
    No downloads, no API calls, no SSL issues.
    Good enough for a demo/learning project."""

    def __init__(self, dimensions: int = 384):
        self.dimensions = dimensions

    def _hash_text(self, text: str) -> List[float]:
        """Convert text to a fixed-size vector using hashing."""
        vector = []
        for i in range(self.dimensions):
            h = hashlib.md5(f"{text}_{i}".encode()).hexdigest()
            value = (int(h[:8], 16) / (2**32)) * 2 - 1  # normalize to [-1, 1]
            vector.append(value)
        # Normalize
        magnitude = sum(v**2 for v in vector) ** 0.5
        if magnitude > 0:
            vector = [v / magnitude for v in vector]
        return vector

    def embed_documents(self, texts: List[str]) -> List[List[float]]:
        return [self._hash_text(text) for text in texts]

    def embed_query(self, text: str) -> List[float]:
        return self._hash_text(text)


# Use simple hash embeddings — NO downloads, NO API calls!
embedding_function = SimpleHashEmbeddings(dimensions=384)

# Initialize Chroma vector store
vectorstore = Chroma(
    persist_directory="./chroma_db",
    embedding_function=embedding_function
)


def load_and_split_document(file_path: str) -> List[Document]:
    if file_path.endswith('.pdf'):
        loader = PyPDFLoader(file_path)
    elif file_path.endswith('.docx'):
        loader = Docx2txtLoader(file_path)
    elif file_path.endswith('.html'):
        loader = UnstructuredHTMLLoader(file_path)
    else:
        raise ValueError(f"Unsupported file type: {file_path}")

    documents = loader.load()
    return text_splitter.split_documents(documents)


def index_document_to_chroma(file_path: str, file_id: int) -> bool:
    try:
        splits = load_and_split_document(file_path)

        for split in splits:
            split.metadata['file_id'] = file_id

        vectorstore.add_documents(splits)
        return True
    except Exception as e:
        print(f"Error indexing document: {e}")
        return False


def delete_doc_from_chroma(file_id: int):
    try:
        docs = vectorstore.get(where={"file_id": file_id})
        print(f"Found {len(docs['ids'])} document chunks for file_id {file_id}")

        vectorstore._collection.delete(where={"file_id": file_id})
        print(f"Deleted all documents with file_id {file_id}")

        return True
    except Exception as e:
        print(f"Error deleting document with file_id {file_id} from Chroma: {str(e)}")
        return False