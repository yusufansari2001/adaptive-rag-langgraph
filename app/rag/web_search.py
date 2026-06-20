from tavily import TavilyClient

from app.config.settings import settings
from app.llm.groq_client import llm


def answer_with_web_search(question: str) -> str:
    """
    Search the web using Tavily and answer using the retrieved content.
    """

    tavily_client = TavilyClient(
        api_key=settings.TAVILY_API_KEY
    )

    response = tavily_client.search(
        query=question,
        max_results=5
    )

    results = response.get("results", [])

    context = "\n\n".join(
        result.get("content", "")
        for result in results
    )

    prompt = f"""
Answer the question using the web search results below.

Question:
{question}

Web Results:
{context}

Instructions:
- Use the web results.
- If the answer cannot be determined, say so.
- Keep the answer concise.
"""

    answer = llm.invoke(prompt)

    return answer.content