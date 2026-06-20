from langgraph.graph import StateGraph, END

from app.graph.state import GraphState
from app.graph.nodes import (
    router_node,
    llm_node,
    web_node,
    query_rewriter_node,
    retriever_node,
    grader_node,
    generator_node
)
from app.graph.routes import (
    route_after_router,
    route_after_grader
)


def build_graph():
    """
    Build and compile the LangGraph workflow.
    """

    graph = StateGraph(GraphState)

    # ==========================
    # Nodes
    # ==========================
    graph.add_node("router", router_node)

    graph.add_node("llm", llm_node)
    graph.add_node("web", web_node)

    graph.add_node("query_rewriter", query_rewriter_node)
    graph.add_node("retriever", retriever_node)
    graph.add_node("grader", grader_node)
    graph.add_node("generate", generator_node)

    # ==========================
    # Entry Point
    # ==========================
    graph.set_entry_point("router")

    # ==========================
    # Router Branches
    # ==========================
    graph.add_conditional_edges(
        "router",
        route_after_router,
        {
            "llm": "llm",
            "web": "web",
            "retriever": "query_rewriter"
        }
    )

    # ==========================
    # RAG Branch
    # ==========================
    graph.add_edge(
        "query_rewriter",
        "retriever"
    )

    graph.add_edge(
        "retriever",
        "grader"
    )

    graph.add_conditional_edges(
        "grader",
        route_after_grader,
        {
            "generate": "generate",
            "web": "web"
        }
    )

    # ==========================
    # End Nodes
    # ==========================
    graph.add_edge("llm", END)
    graph.add_edge("web", END)
    graph.add_edge("generate", END)

    return graph.compile()