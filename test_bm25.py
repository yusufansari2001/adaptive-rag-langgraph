from app.vectorstore.bm25_retriever import retrieve_bm25

results = retrieve_bm25(
    "experiment 6"
)

for i, (doc, score) in enumerate(
    results,
    start=1
):
    print(f"\n===== RESULT {i} =====")
    print(f"Score: {score}")
    print(doc.page_content[:300])