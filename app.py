import streamlit as st
from huggingface_hub import InferenceClient
from io import BytesIO


# -----------------------------
# Page configuration
# -----------------------------

st.set_page_config(
    page_title="AI Text-to-Image Generator",
    page_icon="🎨",
    layout="centered"
)


# -----------------------------
# App title
# -----------------------------

st.title("🎨 AI Text-to-Image Generator")

st.write(
    "Turn your imagination into images with AI."
)


# -----------------------------
# Get Hugging Face token
# -----------------------------

HF_TOKEN = st.secrets["HF_TOKEN"]


# -----------------------------
# Hugging Face model
# -----------------------------

MODEL_ID = "black-forest-labs/FLUX.1-schnell"


# -----------------------------
# Create Hugging Face client
# -----------------------------

client = InferenceClient(
    api_key=HF_TOKEN,
    provider="auto"
)


# -----------------------------
# Prompt input
# -----------------------------

prompt = st.text_area(
    "Describe the image you want to create",
    placeholder=(
        "Example: A beautiful futuristic city at sunset, "
        "with flying cars and cinematic lighting"
    ),
    height=150
)


# -----------------------------
# Generate image
# -----------------------------

if st.button("✨ Generate Image", use_container_width=True):

    if not prompt.strip():

        st.warning("Please enter a prompt.")

    else:

        try:

            with st.spinner("🎨 Generating your image..."):

                image = client.text_to_image(
                    prompt=prompt,
                    model=MODEL_ID
                )

            st.success("Image generated successfully!")

            # Display image
            st.image(
                image,
                caption="Generated Image",
                use_container_width=True
            )

            # Prepare image for download
            image_buffer = BytesIO()

            image.save(
                image_buffer,
                format="PNG"
            )

            image_bytes = image_buffer.getvalue()

            # Download button
            st.download_button(
                label="⬇️ Download Image",
                data=image_bytes,
                file_name="generated_image.png",
                mime="image/png",
                use_container_width=True
            )

        except Exception as e:

            st.error(
                "Something went wrong while generating the image."
            )

            st.error(str(e))
