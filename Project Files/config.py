import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()


class Settings:
    """
    Centralized configuration for the application.
    Reads all required values from the .env file.
    """

    # Application
    APP_NAME = os.getenv("APP_NAME", "AI Marketing Campaign Generator")
    APP_VERSION = os.getenv("APP_VERSION", "1.0.0")

    # Server
    HOST = os.getenv("HOST", "127.0.0.1")
    PORT = int(os.getenv("PORT", 8000))

    # API Keys
    DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")

    # API Endpoints
    DEEPSEEK_BASE_URL = "https://api.deepseek.com/chat/completions"

    GROQ_BASE_URL = "https://api.groq.com/openai/v1/chat/completions"

    # Preferred models
    DEEPSEEK_CHAT_MODEL = "deepseek-chat"
    DEEPSEEK_REASONER_MODEL = "deepseek-reasoner"

    GROQ_LLAMA_MODEL = "llama-3.3-70b-versatile"
    GROQ_QWEN_MODEL = "qwen/qwen3-32b"
    GROQ_MISTRAL_MODEL = "mistral-saba-24b"

    @classmethod
    def validate(cls):
        """
        Ensures all required API keys are available before the app starts.
        """
        missing = []

        if not cls.DEEPSEEK_API_KEY:
            missing.append("DEEPSEEK_API_KEY")

        if not cls.GROQ_API_KEY:
            missing.append("GROQ_API_KEY")

        if missing:
            raise ValueError(
                f"Missing environment variables: {', '.join(missing)}"
            )


# Validate configuration immediately when imported.
Settings.validate()