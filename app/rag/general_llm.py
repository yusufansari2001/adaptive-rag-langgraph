from app.llm.groq_client import llm


def answer_with_llm(question: str) -> str:
    """
    Answer using general LLM knowledge.
    """

    response = llm.invoke(question)

    return response.content