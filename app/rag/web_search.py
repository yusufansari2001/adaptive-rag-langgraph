from tavily import TavilyClient

from app.config.settings import settings
from app.llm.groq_client import llm
from app.prompts.web_search import WEB_SEARCH_PROMPT


MAX_TAVILY_QUERY_LENGTH = 400
NO_CHAT_HISTORY = "No previous conversation."


def _normalize_query_text(text: str) -> str:
    return " ".join(text.split())


def _truncate_query(
    text: str,
    max_length: int = MAX_TAVILY_QUERY_LENGTH
) -> str:
    text = _normalize_query_text(text)

    if len(text) <= max_length:
        return text

    truncated = text[:max_length].rsplit(" ", 1)[0]

    return truncated or text[:max_length]


def _build_search_query(
    question: str,
    chat_history: str
) -> str:
    question = _normalize_query_text(question)

    if chat_history == NO_CHAT_HISTORY:
        return _truncate_query(question)

    prefix = " Context: "
    remaining_length = (
        MAX_TAVILY_QUERY_LENGTH
        - len(question)
        - len(prefix)
    )

    if remaining_length < 40:
        return _truncate_query(question)

    compact_history = _truncate_query(
        chat_history,
        max_length=remaining_length
    )

    return _truncate_query(
        f"{question}{prefix}{compact_history}"
    )


def answer_with_web_search(
    question: str,
    chat_history: str = "No previous conversation."
) -> str:
    """
    Search the web using Tavily and answer using the retrieved content.
    """

    tavily_client = TavilyClient(
        api_key=settings.TAVILY_API_KEY
    )

    response = tavily_client.search(
        query=_build_search_query(
            question=question,
            chat_history=chat_history
        ),
        max_results=5
    )

    results = response.get("results", [])

    context = "\n\n".join(
        result.get("content", "")
        for result in results
    )

    prompt = WEB_SEARCH_PROMPT.format(
        question=question,
        chat_history=chat_history,
        context=context
    )

    answer = llm.invoke(prompt)

    return answer.content
