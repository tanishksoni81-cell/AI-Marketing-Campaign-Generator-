# AI-Marketing-Campaign-Generator-
AI-powered multi-LLM marketing campaign generator that creates optimized content for Google Ads, social media, email, SEO, and CTAs using Python, FastAPI, Streamlit, DeepSeek, and Groq.

The system uses different Large Language Models for different marketing tasks and exposes the AI engine through a FastAPI backend with a Streamlit-based frontend.

---

## 📌 Project Overview

Marketing teams often need to create content for multiple platforms such as:

- Google Ads
- Facebook Ads
- Instagram
- LinkedIn
- Email Marketing
- SEO
- Call-to-Actions

Creating each asset manually takes time and requires different types of copywriting expertise.

This project solves that problem by allowing a marketer to enter basic product information once and automatically generate a complete marketing campaign using multiple LLMs.

---

# 🎯 Objectives

The main objectives of this project are:

- Build a real-world LLM application
- Implement multi-LLM routing
- Separate AI logic from API logic
- Use structured request/response validation
- Build a reusable backend service
- Create a simple business-oriented frontend
- Secure API credentials using environment variables
- Demonstrate an industry-style AI application architecture

---

# ✨ Features

## Multi-LLM Routing

Different marketing tasks can be routed to different models.

Example:

| Marketing Task | LLM |
|---|---|
| Google Ads | DeepSeek |
| Facebook Ads | Llama |
| Instagram | Qwen |
| LinkedIn | Mistral |
| Email Marketing | DeepSeek |
| SEO | Qwen |
| CTA | Llama |

The model configuration can be changed without changing the overall application architecture.

---

## 📢 Marketing Assets

The application generates:

### Google Ads
- Headlines
- Descriptions
- Conversion-focused copy

### Facebook Ads
- Primary text
- Headline
- Description
- CTA

### Instagram
- Caption
- Hook
- Hashtags
- CTA

### LinkedIn
- Professional marketing post
- Value proposition
- CTA

### Email Marketing
- Subject line
- Email body
- CTA

### SEO
- SEO title
- Meta description
- Focus keyword

### CTA
- Multiple call-to-action suggestions

---

# 🏗️ Architecture

```text
                    ┌──────────────────────┐
                    │     Streamlit UI     │
                    │      Frontend        │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │      FastAPI         │
                    │       Backend        │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │  Marketing Service   │
                    │    Business Logic    │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │   Prompt Library     │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │     LLM Router       │
                    └──────────┬───────────┘
                               │
                  ┌────────────┴────────────┐
                  ▼                         ▼
          ┌──────────────┐          ┌──────────────┐
          │   DeepSeek   │          │     Groq     │
          │     API      │          │     API      │
          └──────────────┘          └──────────────┘
