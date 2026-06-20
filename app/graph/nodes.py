from app.rag.router import classify_query
from app.rag.general_llm import answer_with_llm
from app.rag.web_search import answer_with_web_search
from app.rag.grader import grade_documents
from app.rag.generator import generate_answer
from app.rag.query_rewriter import rewrite_query
from app.vectorstore.retriever import retrieve_documents


def router_node(state):
    question = state["question"]

    route = classify_query(question)

    return {
        "route": route.route
    }


def llm_node(state):
    question = state["question"]

    answer = answer_with_llm(question)

    return {
        "answer": answer
    }


def web_node(state):
    question = state["question"]

    answer = answer_with_web_search(question)

    return {
        "answer": answer
    }


def query_rewriter_node(state):
    """
    Rewrite query before retrieval.
    """

    question = state["question"]

    rewritten_question = rewrite_query(question)

    print("\nOriginal Question:")
    print(question)

    print("\nRewritten Question:")
    print(rewritten_question)

    return {
        "rewritten_question": rewritten_question
    }


def retriever_node(state):
    """
    Retrieve using rewritten query.
    """

    query = state["rewritten_question"]

    results = retrieve_documents(query)

    context_parts = []

    for doc, score in results:
        context_parts.append(doc.page_content)

    context = "\n\n".join(context_parts)

    return {
        "context": context
    }


def grader_node(state):
    question = state["question"]
    context = state["context"]

    grade = grade_documents(
        question=question,
        context=context
    )

    return {
        "grade": grade.relevant
    }


def generator_node(state):
    question = state["question"]
    context = state["context"]

    answer = generate_answer(
        question=question,
        context=context
    )

    return {
        "answer": answer
    }