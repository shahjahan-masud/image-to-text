from huggingface_hub import InferenceClient

MODEL_ID = "black-forest-labs/FLUX.1-schnell"

client = InferenceClient(
    api_key=HF_TOKEN,
    provider="auto"
)

image = client.text_to_image(
    prompt="A beautiful futuristic city at sunset, cinematic lighting",
    model=MODEL_ID
)

image
