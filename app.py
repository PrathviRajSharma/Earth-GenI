import gradio as gr
import requests
from PIL import Image
from io import BytesIO

# Function to generate an image (you can replace this with your AI model logic)
def generate_image(prompt):
    # For demonstration, we're using a placeholder image generator
    image_url = f"https://via.placeholder.com/500.png?text={prompt}"
    response = requests.get(image_url)
    img = Image.open(BytesIO(response.content))
    return img

# Create the Gradio interface
interface = gr.Interface(fn=generate_image, inputs="text", outputs="image")

# Launch the app and make it publicly available
interface.launch(server_name="0.0.0.0", server_port=8080)
