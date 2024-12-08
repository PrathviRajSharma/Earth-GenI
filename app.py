import gradio as gr
import requests
from PIL import Image
from io import BytesIO

# Define the Hugging Face API URL
HUGGINGFACE_API_URL = "https://api-inference.huggingface.co/models/sd-legacy/stable-diffusion-v1-5"  # Update with your chosen model
HUGGINGFACE_API_TOKEN = "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"  # Replace with your Hugging Face API token

# Function to generate image using Hugging Face API (Stable Diffusion)
def generate_image(prompt, num_images=1, width=512, height=512):
    headers = {
        "Authorization": "Bearer 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",
        "Content-Type": "application/json",
    }
    
    # Prepare the request data (Hugging Face API expects 'inputs' to be in the body)
    data = {
        "inputs": prompt,
        "options": {
            "use_gpu": True
        },
        "parameters": {
            "num_images": num_images,
            "height": height,
            "width": width
        }
    }

    # Send the request to Hugging Face API
    response = requests.post(HUGGINGFACE_API_URL, json=data, headers=headers)

    if response.status_code == 200:
        images = response.json()['generated_images']  # Depending on the model response
        # Fetch images from the response
        image_objects = []
        for image_data in images:
            img = Image.open(BytesIO(requests.get(image_data['url']).content))
            image_objects.append(img)
        return image_objects
    else:
        return f"Error: {response.status_code} - {response.text}"

# Create Gradio interface for image generation
def create_interface():
    interface = gr.Interface(
        fn=generate_image,
        inputs=[
            gr.Textbox(label="Enter a Prompt", placeholder="e.g. a beautiful sunset over the ocean"),
            gr.Slider(minimum=1, maximum=4, step=1, label="Number of Images", default=1),
            gr.Slider(minimum=256, maximum=1024, step=128, label="Width", default=512),
            gr.Slider(minimum=256, maximum=1024, step=128, label="Height", default=512)
        ],
        outputs="image",
        title="Realistic Image Generation with Stable Diffusion",
        description="Generate realistic images based on your text prompts. You can specify the number of images and their dimensions.",
        live=True
    )
    return interface

# Launch the Gradio interface
if __name__ == "__main__":
    interface = create_interface()
    interface.launch(server_name="0.0.0.0", server_port=10000, share=True)
