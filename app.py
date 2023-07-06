from flask import Flask, render_template, request
import torch
from torchvision.transforms import functional as F
from PIL import Image
import io

app = Flask(__name__)

def civitai_load_model(model_path):
    # Load the model
    model = torch.jit.load(model_path, map_location=torch.device('cpu'))
    model.eval()
    return model

# Load the model
model = civitai_load_model('path_to_model/CommonTaiwaneseFood_24.safetensors')
model.eval()


def generate_image(text):
    # Process the text (if necessary) and generate an image using the model
    # Modify this function based on Civitai's instructions for using their model
    # The following code is just a placeholder
    image = Image.new('RGB', (256, 256), color=(255, 255, 255))
    tensor = F.to_tensor(image)
    prediction = model(tensor)
    generated_image = F.to_pil_image(prediction)

    # Convert the image to bytes
    image_bytes = io.BytesIO()
    generated_image.save(image_bytes, format='PNG')
    image_bytes = image_bytes.getvalue()

    return image_bytes


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Get the text input from the form
        text = request.form['text']

        # Generate an image using the Civitai model
        image = generate_image(text)

        # Render the result in the HTML template
        return render_template('result.html', text=text, image=image)

    # Render the initial HTML form
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
