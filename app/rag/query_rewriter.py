from langchain_core.prompts import PromptTemplate

from app.llm.groq_client import llm
from app.prompts.query_rewriter import QUERY_REWRITER_PROMPT


def rewrite_query(question: str) -> str:
    """
    Rewrite a question to improve retrieval.
    """

    prompt = PromptTemplate(
        template=QUERY_REWRITER_PROMPT,
        input_variables=["question"]
    )

    chain = prompt | llm

    response = chain.invoke(
        {
            "question": question
        }
    )

    return response.content.strip()