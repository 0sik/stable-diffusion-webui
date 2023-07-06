from flask import Flask, render_template, request
import torch
from torchvision.transforms import functional as F
from PIL import Image
import io

app = Flask(__name__)

def civitai_load_model(model_path):

    model = torch.jit.load(model_path, map_location=torch.device('cpu'))
    model.eval()
    return model


model = civitai_load_model('path_to_model/CommonTaiwaneseFood_24.safetensors')
model.eval()


def generate_image(text):

    image = Image.new('RGB', (256, 256), color=(255, 255, 255))
    tensor = F.to_tensor(image)
    prediction = model(tensor)
    generated_image = F.to_pil_image(prediction)

    image_bytes = io.BytesIO()
    generated_image.save(image_bytes, format='PNG')
    image_bytes = image_bytes.getvalue()

    return image_bytes


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
 
        text = request.form['text']

        image = generate_image(text)


        image = generate_image(text)

        return render_template('result.html', text=text, image=image)

    # Render the initial HTML form
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
