from langchain_community.vectorstores import FAISS

from app.vectorstore.embeddings import get_embedding_model
from app.vectorstore.bm25_retriever import retrieve_bm25


def create_vectorstore(chunks):
    """
    Create a FAISS vector store from chunks.
    """

    embedding_model = get_embedding_model()

    vectorstore = FAISS.from_documents(
        documents=chunks,
        embedding=embedding_model
    )

    return vectorstore


def save_vectorstore(vectorstore):
    """
    Save FAISS index locally.
    """

    vectorstore.save_local("vector_store")


def load_vectorstore():
    """
    Load FAISS index from disk.
    """

    embedding_model = get_embedding_model()

    vectorstore = FAISS.load_local(
        "vector_store",
        embedding_model,
        allow_dangerous_deserialization=True
    )

    return vectorstore


def retrieve_documents(query: str, k: int = 10):
    """
    Hybrid Retrieval:
    FAISS + BM25
    """

    vectorstore = load_vectorstore()

    faiss_results = vectorstore.similarity_search_with_score(
        query=query,
        k=5
    )

    bm25_results = retrieve_bm25(
        query=query,
        k=5
    )

    combined = []

    seen = set()

    for doc, score in faiss_results:

        content = doc.page_content

        if content not in seen:
            seen.add(content)
            combined.append((doc, score))

    for doc, score in bm25_results:

        content = doc.page_content

        if content not in seen:
            seen.add(content)
            combined.append((doc, score))

    return combined