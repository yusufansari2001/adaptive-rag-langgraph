def route_after_router(state):

    route = state["route"]

    if route == "rag":
        return "rag"

    if route == "web":
        return "web"

    return "llm"


def route_after_grader(state):

    grade = state.get("grade")

    if grade and grade.lower() == "yes":
        return "generate"

    return "web"
