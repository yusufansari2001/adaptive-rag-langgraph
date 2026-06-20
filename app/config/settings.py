from dotenv import load_dotenv
import os

load_dotenv()


class Settings:
    """
    Centralized application configuration.
    """

    GROQ_API_KEY = os.getenv("GROQ_API_KEY")

    TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

    MODEL_NAME = os.getenv(
        "MODEL_NAME",
        "llama-3.3-70b-versatile"
    )

    CHUNK_SIZE = int(
        os.getenv("CHUNK_SIZE", 1000)
    )

    CHUNK_OVERLAP = int(
        os.getenv("CHUNK_OVERLAP", 200)
    )


settings = Settings()