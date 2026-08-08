"""
llm_router.py
----------------------------
Centralized LLM Router

Supports:
- OpenAI
- Groq
- DeepSeek

"""

from langchain_openai import ChatOpenAI

from config import Settings


class LLMRouter:
    """
    Returns configured LLM instances.
    """

    @staticmethod
    def groq(
        model: str = "llama-3.3-70b-versatile",
        temperature: float = 0.7,
        max_tokens: int = 2048,
    ):
        return ChatOpenAI(
            api_key=Settings.GROQ_API_KEY,
            base_url="https://api.groq.com/openai/v1",
            model=model,
            temperature=temperature,
            max_tokens=max_tokens,
        )

    @staticmethod
    def deepseek(
        model: str = "deepseek-chat",
        temperature: float = 0.7,
        max_tokens: int = 2048,
    ):
        return ChatOpenAI(
            api_key=Settings.DEEPSEEK_API_KEY,
            base_url="https://api.deepseek.com",
            model=model,
            temperature=temperature,
            max_tokens=max_tokens,
        )

    @staticmethod
    def openai(
        model: str = "gpt-4.1-mini",
        temperature: float = 0.7,
        max_tokens: int = 2048,
    ):
        return ChatOpenAI(
            api_key=Settings.OPENAI_API_KEY,
            model=model,
            temperature=temperature,
            max_tokens=max_tokens,
        )

    @staticmethod
    def get_llm(provider: str):
        """
        Factory method.

        Example:
            llm = LLMRouter.get_llm("groq")
        """

        provider = provider.lower()

        providers = {
            "groq": LLMRouter.groq,
            "deepseek": LLMRouter.deepseek,
            "openai": LLMRouter.openai,
        }

        if provider not in providers:
            raise ValueError(
                f"Unsupported provider '{provider}'. "
                f"Choose from: {list(providers.keys())}"
            )

        return providers[provider]()