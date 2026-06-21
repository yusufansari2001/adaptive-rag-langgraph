from langchain_core.prompts import PromptTemplate

from app.llm.groq_client import llm
from app.prompts.generator import GENERATOR_PROMPT


def generate_answer(
    question: str,
    context: str,
    chat_history: str = "No previous conversation."
):
    """
    Generate answer using retrieved context.
    """

    prompt = PromptTemplate(
        template=GENERATOR_PROMPT,
        input_variables=[
            "question",
            "context",
            "chat_history"
        ]
    )

    chain = prompt | llm

    response = chain.invoke(
        {
            "question": question,
            "context": context,
            "chat_history": chat_history
        }
    )

    return response.content
