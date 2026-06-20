import os
import shutil

from app.vectorstore.ingest import (
    load_pdf,
    split_documents
)

from app.vectorstore.retriever import (
    create_vectorstore,
    save_vectorstore
)


UPLOAD_DIR = "uploads"


def upload_pdf(file_path: str):
    """
    Upload PDF and rebuild FAISS index.
    """

    os.makedirs(
        UPLOAD_DIR,
        exist_ok=True
    )

    filename = os.path.basename(
        file_path
    )

    destination = os.path.join(
        UPLOAD_DIR,
        filename
    )

    if file_path != destination:
        shutil.copy(
            file_path,
            destination
        )

    documents = load_pdf(
        destination
    )

    chunks = split_documents(
        documents
    )

    vectorstore = create_vectorstore(
        chunks
    )

    save_vectorstore(
        vectorstore
    )

    return {
        "message": "Document uploaded successfully",
        "file": filename,
        "chunks": len(chunks)
    }