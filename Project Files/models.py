"""
Pydantic Models

Defines request and response schemas
used throughout the application.
"""

from pydantic import BaseModel, Field


# =====================================================
# INPUT MODEL
# =====================================================

class MarketingRequest(BaseModel):
    company: str = Field(..., example="Nike")
    product: str = Field(..., example="Running Shoes")
    audience: str = Field(..., example="Fitness Enthusiasts")
    tone: str = Field(..., example="Professional")
    goal: str = Field(..., example="Increase Sales")


# =====================================================
# OUTPUT MODEL
# =====================================================

class MarketingResponse(BaseModel):
    google_ads: str
    facebook_ads: str
    instagram_caption: str
    linkedin_post: str
    email_marketing: str
    seo_content: str
    cta: str


# =====================================================
# HEALTH CHECK MODEL
# =====================================================

class HealthResponse(BaseModel):
    status: str
    app_name: str
    version: str