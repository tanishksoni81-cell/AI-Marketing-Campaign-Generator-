import streamlit as st
import requests
import json

API_URL = "http://127.0.0.1:8000/generate-campaign"

st.set_page_config(
    page_title="AI Marketing Generator",
    page_icon="🚀",
    layout="wide"
)

st.title("🚀 AI Marketing Campaign Generator")

st.write(
    "Generate complete marketing campaigns using multiple LLM models."
)

st.divider()

col1, col2 = st.columns(2)

with col1:

    company = st.text_input(
        "Company Name"
    )

    product = st.text_input(
        "Product"
    )

    audience = st.text_input(
        "Target Audience"
    )

with col2:

    tone = st.selectbox(
        "Tone",
        [
            "Professional",
            "Friendly",
            "Luxury",
            "Funny",
            "Corporate",
            "Casual"
        ]
    )

    goal = st.text_input(
        "Marketing Goal"
    )

st.divider()

generate = st.button(
    "🚀 Generate Campaign",
    use_container_width=True
)

if generate:

    payload = {

        "company": company,
        "product": product,
        "audience": audience,
        "tone": tone,
        "goal": goal

    }

    with st.spinner("Generating Campaign..."):

        response = requests.post(
            API_URL,
            json=payload
        )

        if response.status_code == 200:

            data = response.json()

            st.success("Campaign Generated Successfully!")

            st.divider()

            sections = [

                ("📢 Google Ads", "google_ads"),

                ("📱 Facebook Ads", "facebook_ads"),

                ("📸 Instagram Caption", "instagram_caption"),

                ("💼 LinkedIn Post", "linkedin_post"),

                ("📧 Email Marketing", "email_marketing"),

                ("🔍 SEO", "seo_content"),

                ("🔥 CTA", "cta")

            ]

            for title, key in sections:

                with st.expander(title, expanded=True):

                    st.text_area(
                        "",
                        data[key],
                        height=220,
                        key=key
                    )

            st.download_button(

                "⬇ Download JSON",

                json.dumps(
                    data,
                    indent=4
                ),

                "campaign.json",

                "application/json"

            )

            txt = ""

            for k, v in data.items():

                txt += f"{k.upper()}\n\n"

                txt += v

                txt += "\n\n"

            st.download_button(

                "⬇ Download TXT",

                txt,

                "campaign.txt"

            )

        else:

            st.error(
                response.text
            )