from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

from app.config.settings import settings


def load_pdf(pdf_path: str):
    """
    Load a PDF file and return LangChain Documents.

    Args:
        pdf_path: Path to the PDF file

    Returns:
        List of LangChain Document objects
    """

    loader = PyPDFLoader(pdf_path)

    documents = loader.load()

    return documents


def split_documents(documents):
    """
    Split documents into smaller chunks.

    Args:
        documents: List of LangChain Documents

    Returns:
        List of chunked Documents
    """

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=settings.CHUNK_SIZE,
        chunk_overlap=settings.CHUNK_OVERLAP
    )

    chunks = text_splitter.split_documents(documents)

    return chunks