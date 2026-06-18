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