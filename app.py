import gradio as gr
import requests
from PIL import Image
from io import BytesIO

# Your AI logic here (replace this with actual logic)
def generate_image(prompt):
    image_url = f"https://via.placeholder.com/500.png?text={prompt}"
    response = requests.get(image_url)
    img = Image.open(BytesIO(response.content))
    return img

# Create the Gradio interface
interface = gr.Interface(fn=generate_image, inputs="text", outputs="image")

# Launch the Gradio app with Flask
interface.launch(server_name="0.0.0.0", server_port=8080, share=True)
