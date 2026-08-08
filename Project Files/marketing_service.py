"""
marketing_service.py

Business Logic Layer

Responsibilities:
1. Receive validated request
2. Generate prompts
3. Route prompts to different LLMs
4. Collect responses
5. Return structured output
"""

from llm_router import LLMRouter

from prompt import (
    google_ads_prompt,
    facebook_ads_prompt,
    instagram_caption_prompt,
    linkedin_post_prompt,
    email_marketing_prompt,
    seo_prompt,
    cta_prompt,
)

from models import (
    MarketingRequest,
    MarketingResponse,
)


class MarketingService:

    def __init__(self):
        # Create LLM instances only once
        self.groq_llm = LLMRouter.get_llm("groq")
        self.deepseek_llm = LLMRouter.get_llm("deepseek")

    def _generate(self, llm, prompt: str) -> str:
        """
        Helper function to call any LLM safely.
        """
        try:
            response = llm.invoke(prompt)

            if hasattr(response, "content"):
                return response.content.strip()

            return str(response)

        except Exception as e:
            return f"Generation Error: {str(e)}"

    def generate_campaign(
        self,
        request: MarketingRequest
    ) -> MarketingResponse:

        # ----------------------------
        # Build Prompts
        # ----------------------------

        google_prompt = google_ads_prompt(
            request.product,
            request.company,
            request.audience,
            request.tone,
            request.goal,
        )

        facebook_prompt = facebook_ads_prompt(
            request.product,
            request.company,
            request.audience,
            request.tone,
            request.goal,
        )

        instagram_prompt = instagram_caption_prompt(
            request.product,
            request.company,
            request.audience,
            request.tone,
            )

        linkedin_prompt = linkedin_post_prompt(
            request.product,
            request.company,
            request.audience,
            request.tone,
            )

        email_prompt = email_marketing_prompt(
            request.product,
            request.company,
            request.audience,
            request.tone,
            )

        seo_content_prompt = seo_prompt(
            request.product,
            request.company,
            )

        cta_content_prompt = cta_prompt(
            request.product,
            )

        # ----------------------------
        # Multi-LLM Routing
        # ----------------------------

        google_ads = self._generate(
            self.groq_llm,
            google_prompt,
        )

        facebook_ads = self._generate(
            self.groq_llm,
            facebook_prompt,
        )

        instagram_caption = self._generate(
            self.groq_llm,
            instagram_prompt,
        )

        linkedin_post = self._generate(
            self.groq_llm,
            linkedin_prompt,
        )

        email_marketing = self._generate(
            self.groq_llm,
            email_prompt,
        )

        seo_content = self._generate(
            self.groq_llm,
            seo_content_prompt,
        )

        cta = self._generate(
            self.groq_llm,
            cta_content_prompt,
        )

        # ----------------------------
        # Return API Response
        # ----------------------------

        return MarketingResponse(
            google_ads=google_ads,
            facebook_ads=facebook_ads,
            instagram_caption=instagram_caption,
            linkedin_post=linkedin_post,
            email_marketing=email_marketing,
            seo_content=seo_content,
            cta=cta,
        )