"""Generate concise website summaries using a Groq-backed OpenAI-compatible model."""

import os

from dotenv import load_dotenv
from openai import OpenAI

from scraper import fetch_website_contents

# Keep environment configuration in a local .env file for easy public setup.
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
base_url = os.getenv("GROQ_BASE_URL")

if not api_key or not base_url:
    raise RuntimeError(
        "Missing GROQ_API_KEY or GROQ_BASE_URL in your environment or .env file. "
        "Example: GROQ_API_KEY=your_key and GROQ_BASE_URL=https://api.groq.com/openai/v1"
    )

client = OpenAI(
    api_key=api_key,
    base_url=base_url,
)

# This system prompt keeps responses focused, readable, and markdown-friendly.
system_prompt = """You are an intelligent website content summarizer. Analyze
the webpage content and generate a concise, engaging, and easy-to-understand
summary. Ignore navigation menus. Respond in markdown."""


def summarize(url):
    """Return a short markdown summary for the given website URL."""
    website = fetch_website_contents(url)

    try:
        response = client.chat.completions.create(
            model=os.getenv("GROQ_MODEL_ID"),
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": f"Summarize this website:\n\n{website}"},
            ],
        )
        return response.choices[0].message.content or "No summary was generated."
    except Exception as exc:
        # Surface a clear message instead of a raw traceback in the UI.
        return f"Could not generate a summary. Error: {exc}"
