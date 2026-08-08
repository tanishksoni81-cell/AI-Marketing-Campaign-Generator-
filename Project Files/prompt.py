"""
Production Prompt Library

This file contains all prompts used by the AI Marketing Campaign Generator.
Each function returns a prompt string for a specific marketing task.
"""


def google_ads_prompt(product, company, audience, tone, goal):
    return f"""
You are an expert Google Ads copywriter.

Company: {company}
Product: {product}
Target Audience: {audience}
Tone: {tone}
Goal: {goal}

Generate:

1. Headline 1
2. Headline 2
3. Headline 3
4. Description 1
5. Description 2

Keep the copy engaging and conversion-focused.

Return only the final content.
"""


def facebook_ads_prompt(product, company, audience, tone, goal):
    return f"""
You are an expert Facebook Ads strategist.

Company: {company}
Product: {product}
Audience: {audience}
Tone: {tone}
Goal: {goal}

Generate:

- Primary Text
- Headline
- Description
- CTA

Return only the final content.
"""


def instagram_caption_prompt(product, company, audience, tone):
    return f"""
Create a high-performing Instagram caption.

Company: {company}
Product: {product}
Audience: {audience}
Tone: {tone}

Include:

- Attractive Hook
- Caption
- 8 Relevant Hashtags
- CTA

Return only the content.
"""


def linkedin_post_prompt(product, company, audience, tone):
    return f"""
Write a professional LinkedIn marketing post.

Company: {company}
Product: {product}
Audience: {audience}
Tone: {tone}

Include:

- Attention-grabbing opening
- Value proposition
- Call to Action

Return only the content.
"""


def email_marketing_prompt(product, company, audience, tone):
    return f"""
Write a marketing email.

Company: {company}
Product: {product}
Audience: {audience}
Tone: {tone}

Generate:

Subject Line

Email Body

CTA

Return only the email.
"""


def seo_prompt(product, company):
    return f"""
Create SEO content.

Company: {company}
Product: {product}

Generate:

SEO Title

Meta Description (155 characters max)

Focus Keyword

Return only the content.
"""


def cta_prompt(product):
    return f"""
Generate 5 powerful Call-To-Action sentences.

Product:

{product}

Return only the CTAs.
"""