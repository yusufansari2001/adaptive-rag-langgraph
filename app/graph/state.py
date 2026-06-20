from typing import TypedDict, Optional


class GraphState(TypedDict):
    question: str

    route: Optional[str]

    context: Optional[str]

    grade: Optional[str]

    answer: Optional[str]