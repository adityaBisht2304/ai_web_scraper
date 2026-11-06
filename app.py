"""Launch the Gradio interface for the website summarizer."""

# Install the UI dependency before running the app: pip install gradio
import gradio as gr
from summarizer import summarize


# The interface keeps the app easy to use: a URL input and a markdown summary output.
if __name__ == "__main__":
    demo = gr.Interface(
        fn=summarize,
        inputs=gr.Textbox(label="Website URL"),
        outputs=gr.Markdown(label="Summary"),
        title="🔎 AI Website Summarizer",
    )
    # share=True creates a public URL so the app can be shared quickly.
    demo.launch(share=True)