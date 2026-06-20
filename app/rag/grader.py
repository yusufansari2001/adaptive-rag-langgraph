from langchain_core.prompts import PromptTemplate

from app.llm.groq_client import llm
from app.models.grade import GradeDocuments
from app.prompts.grader import GRADER_PROMPT


def grade_documents(question: str, context: str) -> GradeDocuments:
    """
    Grade whether retrieved context is relevant to a question.
    """

    structured_llm = llm.with_structured_output(
        GradeDocuments
    )

    prompt = PromptTemplate(
        template=GRADER_PROMPT,
        input_variables=["question", "context"]
    )

    chain = prompt | structured_llm

    result = chain.invoke(
        {
            "question": question,
            "context": context
        }
    )

    return result