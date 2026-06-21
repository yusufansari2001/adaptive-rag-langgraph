from langchain_core.prompts import PromptTemplate

from app.llm.groq_client import llm
from app.models.route import RouteDecision
from app.prompts.router import ROUTER_PROMPT


def classify_query(
    question: str,
    chat_history: str = "No previous conversation."
) -> RouteDecision:
    """
    Classify user question into:
    rag / web / llm
    """

    structured_llm = llm.with_structured_output(
        RouteDecision
    )

    prompt = PromptTemplate(
        template=ROUTER_PROMPT,
        input_variables=[
            "question",
            "chat_history"
        ]
    )

    chain = prompt | structured_llm

    result = chain.invoke(
        {
            "question": question,
            "chat_history": chat_history
        }
    )

    return result
