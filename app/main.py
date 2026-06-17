from app.llm.groq_client import llm


response = llm.invoke(
    "Explain Spring Boot in one sentence."
)

print(response.content)