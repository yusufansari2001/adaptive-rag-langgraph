from fastapi import APIRouter
from pydantic import BaseModel

from app.graph.builder import build_graph


router = APIRouter()

graph = build_graph()


class QuestionRequest(BaseModel):
    question: str


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