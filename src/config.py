
import os
from dotenv import load_dotenv

load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY", "")
OPENROUTER_BASE_URL = os.getenv("OPENROUTER_BASE_URL", "https://openrouter.ai/api/v1")
OPENROUTER_MODEL = os.getenv("OPENROUTER_MODEL", "deepseek/deepseek-chat-v3-0324:free")

EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "text-embedding-3-small")

DATA_DIR = os.getenv("DATA_DIR", "./data")
REPOS_DIR = os.getenv("REPOS_DIR", "./data/repos")
INDEX_DIR = os.getenv("INDEX_DIR", "./data/index")

ALLOWED_EXTENSIONS = {
    ".py", ".js", ".ts", ".tsx", ".jsx", ".java", ".go", ".rs", ".cpp", ".c",
    ".h", ".hpp", ".cs", ".php", ".rb", ".swift", ".kt", ".kts", ".scala",
    ".md", ".txt", ".json", ".yaml", ".yml", ".toml"
}

