from app.graph.builder import build_graph

graph = build_graph()

while True:

    question = input("\nAsk a question (type 'exit' to quit): ")

    if question.lower() == "exit":
        break

    result = graph.invoke(
        {
            "question": question
        }
    )

    print("\nAnswer:\n")
    print(result["answer"])