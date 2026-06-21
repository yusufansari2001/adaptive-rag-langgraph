from langchain_core.messages import BaseMessage, SystemMessage

from app.llm.groq_client import llm


GENERAL_LLM_SYSTEM_PROMPT = """
You are a helpful assistant.
Use the conversation history to answer follow-up questions naturally.
Keep answers concise unless the user asks for detail.
"""


def answer_with_llm(messages: list[BaseMessage]) -> str:
    """
    Answer using general LLM knowledge and conversation history.
    """

    response = llm.invoke(
        [
            SystemMessage(content=GENERAL_LLM_SYSTEM_PROMPT)
        ]
        + messages
    )

    return response.content
