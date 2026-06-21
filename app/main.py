from langchain_core.messages import HumanMessage

from app.graph.builder import build_graph
from app.graph.message_utils import get_latest_ai_answer

graph = build_graph()
SESSION_ID = "cli"

while True:

    question = input("\nAsk a question (type 'exit' to quit): ")

    if question.lower() == "exit":
        break

    result = graph.invoke(
        {
            "messages": [
                HumanMessage(content=question)
            ]
        },
        config={
            "configurable": {
                "thread_id": SESSION_ID
            }
        }
    )

    print("\nAnswer:\n")
    print(get_latest_ai_answer(result))
