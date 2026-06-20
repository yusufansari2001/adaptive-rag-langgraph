import os

from rank_bm25 import BM25Okapi

from app.vectorstore.ingest import (
    load_pdf,
    split_documents
)


UPLOAD_DIR = "uploads"


def get_latest_uploaded_pdf():
    """
    Get latest uploaded PDF.
    """

    pdf_files = [
        os.path.join(
            UPLOAD_DIR,
            file
        )
        for file in os.listdir(
            UPLOAD_DIR
        )
        if file.endswith(".pdf")
    ]

    if not pdf_files:
        raise ValueError(
            "No uploaded PDF found."
        )

    pdf_files.sort(
        key=os.path.getmtime,
        reverse=True
    )

    return pdf_files[0]


def create_bm25_retriever():
    """
    Create BM25 retriever from latest uploaded PDF.
    """

    latest_pdf = get_latest_uploaded_pdf()

    documents = load_pdf(
        latest_pdf
    )

    chunks = split_documents(
        documents
    )

    tokenized_chunks = [
        chunk.page_content.split()
        for chunk in chunks
    ]

    bm25 = BM25Okapi(
        tokenized_chunks
    )

    return bm25, chunks


def retrieve_bm25(
    query: str,
    k: int = 5
):
    """
    Retrieve top chunks using BM25.
    """

    bm25, chunks = (
        create_bm25_retriever()
    )

    tokenized_query = (
        query.split()
    )

    scores = bm25.get_scores(
        tokenized_query
    )

    ranked = sorted(
        zip(chunks, scores),
        key=lambda x: x[1],
        reverse=True
    )

    return ranked[:k]