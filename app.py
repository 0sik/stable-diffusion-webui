from flask import Flask, render_template, request
import civitia  # Assuming you have the Civitia model implemented

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Get the text input from the form
        text = request.form['text']

        # Generate an image using the Civitia model
        image = civitia.generate_image(text)

        # Render the result in the HTML template
        return render_template('result.html', image=image)

    # Render the initial HTML form
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
