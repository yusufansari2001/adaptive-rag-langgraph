from app.rag.grader import grade_documents


question = "What is Spring Boot?"

context = """
FIRST set contains all terminals that can appear as the first symbol.
FOLLOW set contains all terminals that can appear after a non-terminal.
"""

result = grade_documents(
    question=question,
    context=context
)

print(result)
print()
print(f"Relevant: {result.relevant}")