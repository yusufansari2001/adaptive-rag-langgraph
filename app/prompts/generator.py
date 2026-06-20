GENERATOR_PROMPT = """
You are a helpful assistant.

Answer the user's question using ONLY the provided context.

Question:
{question}

Context:
{context}

Instructions:
- Use only the context.
- If the answer is not in the context, say you do not know.
- Keep the answer concise.
"""