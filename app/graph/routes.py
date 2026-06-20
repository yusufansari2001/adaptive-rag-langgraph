def route_after_router(state):

    route = state["route"]

    if route == "rag":
        return "retriever"

    if route == "web":
        return "web"

    return "llm"


def route_after_grader(state):

    grade = state["grade"]

    if grade.lower() == "yes":
        return "generate"

    return "web"