from langchain_community.vectorstores import FAISS

from app.vectorstore.embeddings import get_embedding_model


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