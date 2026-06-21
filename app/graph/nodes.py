from langchain_core.messages import AIMessage

from app.rag.router import classify_query
from app.rag.general_llm import answer_with_llm
from app.rag.web_search import answer_with_web_search
from app.rag.grader import grade_documents
from app.rag.generator import generate_answer
from app.rag.query_rewriter import rewrite_query
from app.vectorstore.retriever import retrieve_documents
from app.graph.message_utils import (
    format_chat_history,
    get_latest_question
)


def _score_to_float(score):
    try:
        return float(score)
    except (TypeError, ValueError):
        return None


def router_node(state):
    question = get_latest_question(state)
    chat_history = format_chat_history(state)

    route = classify_query(
        question=question,
        chat_history=chat_history
    )
    route_name = route.route.strip().lower()

    return {
        "route": route_name,
        "rewritten_query": None,
        "retrieved_docs": None,
        "context": None,
        "grade": None
    }


def llm_node(state):
    answer = answer_with_llm(
        state["messages"]
    )

    return {
        "messages": [
            AIMessage(content=answer)
        ]
    }


def web_node(state):
    question = get_latest_question(state)
    chat_history = format_chat_history(state)

    answer = answer_with_web_search(
        question=question,
        chat_history=chat_history
    )

    return {
        "messages": [
            AIMessage(content=answer)
        ]
    }


def query_rewriter_node(state):
    """
    Rewrite query before retrieval.
    """

    question = get_latest_question(state)
    chat_history = format_chat_history(state)

    rewritten_query = rewrite_query(
        question=question,
        chat_history=chat_history
    )

    print("\nOriginal Question:")
    print(question)

    print("\nRewritten Query:")
    print(rewritten_query)

    return {
        "rewritten_query": rewritten_query
    }


def retriever_node(state):
    """
    Hybrid Retrieval using FAISS + BM25.
    """

    query = state.get("rewritten_query") or get_latest_question(state)

    results = retrieve_documents(query)

    print("\nRetrieved Documents:")

    context_parts = []
    retrieved_docs = []

    for i, (doc, score) in enumerate(results, start=1):

        print(f"\n===== DOC {i} =====")
        print(f"Score: {score}")
        print(doc.page_content[:300])

        context_parts.append(doc.page_content)
        retrieved_docs.append(
            {
                "content": doc.page_content,
                "metadata": doc.metadata,
                "score": _score_to_float(score)
            }
        )

    context = "\n\n".join(context_parts)

    return {
        "context": context,
        "retrieved_docs": retrieved_docs
    }


def grader_node(state):
    question = state.get("rewritten_query") or get_latest_question(state)
    context = state.get("context") or ""

    grade = grade_documents(
        question=question,
        context=context
    )

    print(f"\nRelevance Score: {grade.relevant}")

    return {
        "grade": grade.relevant
    }


def generator_node(state):
    question = get_latest_question(state)
    context = state.get("context") or ""
    chat_history = format_chat_history(state)

    answer = generate_answer(
        question=question,
        context=context,
        chat_history=chat_history
    )

    return {
        "messages": [
            AIMessage(content=answer)
        ]
    }
