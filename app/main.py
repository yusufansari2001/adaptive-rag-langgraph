from app.vectorstore.ingest import load_pdf, split_documents
from app.vectorstore.retriever import (
    create_vectorstore,
    save_vectorstore
)

documents = load_pdf(
    "data/documents/LAB_RECORDS.pdf"
)

chunks = split_documents(documents)

vectorstore = create_vectorstore(chunks)

save_vectorstore(vectorstore)

print("Vector store saved successfully!")