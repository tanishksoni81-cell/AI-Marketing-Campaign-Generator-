"""
FastAPI Backend

Exposes REST API endpoints for the
AI Marketing Campaign Generator.
"""

from fastapi import FastAPI, HTTPException

from config import Settings
from marketing_service import MarketingService
from models import (
    MarketingRequest,
    MarketingResponse,
    HealthResponse
)

# ----------------------------------------------------
# FastAPI App
# ----------------------------------------------------

app = FastAPI(
    title=Settings.APP_NAME,
    version=Settings.APP_VERSION,
    description="Multi-LLM AI Marketing Campaign Generator"
)

# ----------------------------------------------------
# Initialize Service
# ----------------------------------------------------

marketing_service = MarketingService()

# ----------------------------------------------------
# Root Endpoint
# ----------------------------------------------------

@app.get("/")
def root():
    return {
        "message": "Welcome to AI Marketing Campaign Generator",
        "version": Settings.APP_VERSION
    }

# ----------------------------------------------------
# Health Check
# ----------------------------------------------------

@app.get(
    "/health",
    response_model=HealthResponse
)
def health():

    return HealthResponse(
        status="Running",
        app_name=Settings.APP_NAME,
        version=Settings.APP_VERSION
    )

# ----------------------------------------------------
# Generate Marketing Campaign
# ----------------------------------------------------

@app.post(
    "/generate-campaign",
    response_model=MarketingResponse
)
def generate_campaign(
    request: MarketingRequest
):

    try:

        response = marketing_service.generate_campaign(
            request
        )

        return response

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )