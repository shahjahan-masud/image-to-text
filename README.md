# AI Text-to-Image Generator

A simple Streamlit app that turns a text description into an AI-generated image using Hugging Face's Stable Diffusion model.

## Files
- `app.py` — the Streamlit app
- `requirements.txt` — Python packages needed
- `.gitignore` — files GitHub should ignore (keeps your secret key safe)

## Setup
1. Get a free Hugging Face account and API token: https://huggingface.co/settings/tokens
2. Add your token as a secret named `HF_TOKEN`:
   - Locally: create `.streamlit/secrets.toml` with `HF_TOKEN = "your_token_here"`
   - On Streamlit Community Cloud: add it in the app's "Secrets" settings
3. Install dependencies: `pip install -r requirements.txt`
4. Run the app: `streamlit run app.py`
