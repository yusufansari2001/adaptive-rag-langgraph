from typing import Any

from langgraph.graph import MessagesState


class GraphState(MessagesState):
    route: str | None

    rewritten_query: str | None

    retrieved_docs: list[dict[str, Any]] | None

    context: str | None

    grade: str | None
