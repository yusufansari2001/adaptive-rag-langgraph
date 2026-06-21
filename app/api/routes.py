import uuid
from pathlib import Path

from fastapi import (
    APIRouter,
    UploadFile,
    File
)
from pydantic import BaseModel
from langchain_core.messages import HumanMessage

from app.graph.builder import build_graph
from app.graph.message_utils import get_latest_ai_answer
from app.services.document_upload import (
    upload_pdf
)


router = APIRouter()

graph = build_graph()

UPLOAD_DIR = "uploads"


class QuestionRequest(BaseModel):
    question: str
    session_id: str | None = None


class QuestionResponse(BaseModel):
    answer: str
    session_id: str


@router.post(
    "/ask",
    response_model=QuestionResponse
)
def ask_question(request: QuestionRequest):
    session_id = request.session_id or str(
        uuid.uuid4()
    )

    result = graph.invoke(
        {
            "messages": [
                HumanMessage(content=request.question)
            ]
        },
        config={
            "configurable": {
                "thread_id": session_id
            }
        }
    )

    return QuestionResponse(
        answer=get_latest_ai_answer(result),
        session_id=session_id
    )


@router.post("/upload")
async def upload_document(
    file: UploadFile = File(...)
):

    Path(
        UPLOAD_DIR
    ).mkdir(
        exist_ok=True
    )

    file_path = (
        Path(UPLOAD_DIR)
        / file.filename
    )

    contents = await file.read()

    with open(
        file_path,
        "wb"
    ) as f:
        f.write(contents)

    result = upload_pdf(
        str(file_path)
    )

    return result
