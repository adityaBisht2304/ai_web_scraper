# AI Web Scraper

A lightweight AI-powered web scraper that fetches website content, removes noisy HTML, and produces a short, readable summary in markdown.

## Features

- Fetches a webpage from any public site URL
- Removes navigation, scripts, styles, and decorative HTML blocks
- Extracts meaningful text content and page title
- Sends the cleaned content to a Groq-backed model for a concise summary
- Runs as a simple Gradio app with a public share link option

## Tech Stack

- Python
- requests
- BeautifulSoup
- OpenAI Python SDK
- Gradio
- dotenv

## Prerequisites

- Python 3.10+
- A Groq API key
- Access to a Groq-compatible base URL (for example, `https://api.groq.com/openai/v1`)

## Installation

1. Clone the repository.
2. Create and activate a virtual environment:

   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the project root with your Groq credentials:

   ```env
   GROQ_API_KEY=your_api_key_here
   GROQ_BASE_URL=https://api.groq.com/openai/v1
   ```

## Run the app

Start the interface:

```bash
python app.py
```

Then paste a website URL into the textbox and click submit. The app shows a cleaned summary of the page.

## Project Structure

- `app.py` — Gradio UI entry point
- `scraper.py` — fetches and cleans website content
- `summarizer.py` — sends cleaned text to the LLM for summarization
- `requirements.txt` — Python dependencies

## Notes

- The app currently expects a valid public website URL.
- `share=True` is enabled in the Gradio launch, which makes it easy to share a public demo link.
- Keep your API key in a local `.env` file and do not commit secrets to the repository.

## Example

```text
Input URL: https://www.example.com
Output: A short markdown summary that highlights the main purpose of the page.
```
