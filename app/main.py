from app.vectorstore.ingest import load_pdf, split_documents
from app.vectorstore.retriever import create_vectorstore

documents = load_pdf(
    "data/documents/LAB_RECORDS.pdf"
)

chunks = split_documents(documents)

vectorstore = create_vectorstore(chunks)

print(f"Pages loaded: {len(documents)}")
print(f"Chunks created: {len(chunks)}")

print("\nVector store created successfully!")