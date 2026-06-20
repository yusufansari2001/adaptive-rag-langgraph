GRADER_PROMPT = """
You are a grader assessing whether retrieved context is relevant to a user question.

Question:
{question}

Retrieved Context:
{context}

Instructions:
- If the context contains information that helps answer the question, return yes.
- If the context is unrelated to the question, return no.
- Return only yes or no.
"""