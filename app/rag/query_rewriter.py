from langchain_core.prompts import PromptTemplate

from app.llm.groq_client import llm
from app.prompts.query_rewriter import QUERY_REWRITER_PROMPT


def rewrite_query(
    question: str,
    chat_history: str = "No previous conversation."
) -> str:
    """
    Rewrite a question to improve retrieval.
    """

    prompt = PromptTemplate(
        template=QUERY_REWRITER_PROMPT,
        input_variables=[
            "question",
            "chat_history"
        ]
    )

    chain = prompt | llm

    response = chain.invoke(
        {
            "question": question,
            "chat_history": chat_history
        }
    )

    return response.content.strip()
