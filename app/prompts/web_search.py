WEB_SEARCH_PROMPT = """
You are a helpful assistant.

Answer the latest user question using the web search results below.
Use the conversation history only to understand references in the latest question.

Conversation History:
{chat_history}

Latest Question:
{question}

Web Results:
{context}

Instructions:
- Use the web results.
- If the answer cannot be determined, say so.
- Keep the answer concise.
"""
