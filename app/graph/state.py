from typing import TypedDict, Optional


class GraphState(TypedDict):
    question: str

    rewritten_question: Optional[str]

    route: Optional[str]

    context: Optional[str]

    grade: Optional[str]

    answer: Optional[str]