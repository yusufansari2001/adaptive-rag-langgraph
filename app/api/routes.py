from pathlib import Path

from fastapi import (
    APIRouter,
    UploadFile,
    File
)
from pydantic import BaseModel

from app.graph.builder import build_graph
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


@router.post(
    "/ask",
    response_model=QuestionResponse
)
def ask_question(request: QuestionRequest):

    result = graph.invoke(
        {
            "question": request.question
        }
    )

    return QuestionResponse(
        answer=result["answer"]
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