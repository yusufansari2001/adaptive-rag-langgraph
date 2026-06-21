from langchain_core.messages import HumanMessage

from app.graph.builder import build_graph
from app.graph.message_utils import get_latest_ai_answer


graph = build_graph()


def run_adaptive_rag(
    question: str,
    session_id: str = "default"
):
    """
    Main adaptive rag workflow.
    """

    result = graph.invoke(
        {
            "messages": [
                HumanMessage(content=question)
            ]
        },
        config={
            "configurable": {
                "thread_id": session_id
            }
        }
    )

    return get_latest_ai_answer(result)
