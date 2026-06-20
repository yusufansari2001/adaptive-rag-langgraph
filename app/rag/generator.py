from langchain_core.prompts import PromptTemplate

from app.llm.groq_client import llm
from app.prompts.generator import GENERATOR_PROMPT


def generate_answer(question: str, context: str):
    """
    Generate answer using retrieved context.
    """

    prompt = PromptTemplate(
        template=GENERATOR_PROMPT,
        input_variables=["question", "context"]
    )

    chain = prompt | llm

    response = chain.invoke(
        {
            "question": question,
            "context": context
        }
    )

    return response.content