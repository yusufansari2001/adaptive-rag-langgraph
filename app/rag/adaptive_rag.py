from app.rag.router import classify_query
from app.rag.general_llm import answer_with_llm
from app.rag.grader import grade_documents
from app.rag.generator import generate_answer
from app.rag.web_search import answer_with_web_search
from app.vectorstore.retriever import retrieve_documents


def run_adaptive_rag(question: str):
    """
    Main adaptive rag workflow.
    """

    route = classify_query(question)

    print(f"\nSelected Route: {route.route}")

    # ==========================
    # LLM ROUTE
    # ==========================
    if route.route == "llm":
        return answer_with_llm(question)

    # ==========================
    # WEB ROUTE
    # ==========================
    if route.route == "web":
        return answer_with_web_search(question)

    # ==========================
    # RAG ROUTE
    # ==========================
    if route.route == "rag":

        results = retrieve_documents(question)

        context_parts = []

        for i, (doc, score) in enumerate(results, start=1):
            print(f"\n===== DOC {i} =====")
            print(f"Score: {score}")
            print(doc.page_content[:300])

            context_parts.append(doc.page_content)

        context = "\n\n".join(context_parts)

        grade = grade_documents(
            question=question,
            context=context
        )

        print(f"\nRelevance Score: {grade.relevant}")

        if grade.relevant.lower() == "yes":
            return generate_answer(
                question=question,
                context=context
            )

        return "No relevant information found in the uploaded documents."

    return "Route not implemented."