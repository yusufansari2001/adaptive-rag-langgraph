from pydantic import BaseModel, Field


class RouteDecision(BaseModel):
    """
    Routing decision for adaptive RAG.
    """

    route: str = Field(
        description="""
        Route can be one of:
        - rag
        - web
        - llm
        """
    )