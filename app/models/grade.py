from pydantic import BaseModel, Field


class GradeDocuments(BaseModel):
    """
    Binary relevance score for retrieved documents.
    """

    relevant: str = Field(
        description="Return 'yes' if the context is relevant to the question, otherwise 'no'."
    )