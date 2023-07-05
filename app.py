from flask import Flask, render_template, request
import civitia  

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        text = request.form['text']

        image = civitia.generate_image(text)

        return render_template('result.html', image=image)

    return render_template('index.html')

if __name__ == '__main__':
    app.run()
