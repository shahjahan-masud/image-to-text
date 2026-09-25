import streamlit as st
from huggingface_hub import InferenceClient

# ----------------------------------------------------------
# PAGE SETUP
# ----------------------------------------------------------
st.set_page_config(page_title="AI Image Generator", page_icon="🎨")

st.title("🎨 AI Text-to-Image Generator")
st.write("Type a description below, and AI will create an image for you.")

# ----------------------------------------------------------
# CONFIGURATION
# You can change this to try a different Hugging Face model.
# ----------------------------------------------------------
MODEL_NAME = "stabilityai/stable-diffusion-2-1"

# ----------------------------------------------------------
# LOAD API KEY SECURELY
# This reads the token from Streamlit's secrets manager.
# NEVER type your token directly into this file.
# ----------------------------------------------------------
try:
    HF_TOKEN = st.secrets["HF_TOKEN"]
except Exception:
    st.error(
        "Hugging Face token not found. Please add HF_TOKEN to your "
        "Streamlit secrets (see the setup instructions)."
    )
    st.stop()

# Create the client that talks to Hugging Face's servers
client = InferenceClient(model=MODEL_NAME, token=HF_TOKEN)

# ----------------------------------------------------------
# USER INTERFACE
# ----------------------------------------------------------
prompt = st.text_area(
    "Describe the image you want:",
    placeholder="A cat riding a bicycle on the moon, digital art style",
    height=100,
)

if st.button("Generate Image", type="primary"):
    if not prompt.strip():
        st.warning("Please type a description first.")
    else:
        with st.spinner("Generating your image... this can take up to 30 seconds."):
            try:
                image = client.text_to_image(prompt)
                st.image(image, caption=prompt, use_container_width=True)
            except Exception as e:
                st.error(f"Something went wrong while generating the image: {e}")
