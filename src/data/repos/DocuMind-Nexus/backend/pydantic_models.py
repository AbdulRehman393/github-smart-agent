from pydantic import BaseModel, Field
from enum import Enum
from datetime import datetime


class ModelName(str, Enum):
    NEMOTRON_NANO = "nvidia/nemotron-nano-9b-v2:free"
    QWEN3_4B = "qwen/qwen3-4b:free"
    DEEPSEEK_R1 = "deepseek/deepseek-r1-0528:free"
    MISTRAL_SMALL = "mistralai/mistral-small-3.1-24b-instruct:free"


class AnswerSource(str, Enum):
    DOCUMENT = "document"
    WEB = "web"
    LLM = "llm"
    GREETING = "greeting"


class QueryInput(BaseModel):
    question: str
    session_id: str = Field(default=None)
    model: ModelName = Field(default=ModelName.NEMOTRON_NANO)


class QueryResponse(BaseModel):
    answer: str
    session_id: str
    model: ModelName
    source: AnswerSource = Field(default=AnswerSource.LLM)


class DocumentInfo(BaseModel):
    id: int
    filename: str
    upload_timestamp: datetime


class DeleteFileRequest(BaseModel):
    file_id: int