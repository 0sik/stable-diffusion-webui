rom flask import Flask, render_template, request
 
app = Flask(__name__)
 
@app.route("/",  methods=['GET', 'POST'])
 
def index():
 
    name=""
 
    if request.method == 'POST':
        name = request.form.get("name", "홍길동")
 
    return render_template('6_post_get.html', name = name)
 
if __name__ == "__main__"

rom flask import Flask, render_template, request
 
app = Flask(__name__)
 
@app.route("/",  methods=['GET', 'POST'])
 
def index():
 
    name=""
 
    if request.method == 'POST':
        name = request.form.get("name", "홍길동")
 
    return render_template('6_post_get.html', name = name)
 
if __name__ == "__main__"

from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def index():
    return render_template("index.html")
if __name__ == '__main__':
    app.run(debug=True)
    
from flask import Flask, render_template

app = Flask(__name__)

student_data = {
    1: {"name": "슈퍼맨", "score": {"국어": 90, "수학": 65}},
    2: {"name": "배트맨", "score": {"국어": 75, "영어": 80, "수학": 75}}
}

@app.route('/')
def index():
    return render_template("index.html", 
            template_students = student_data)

@app.route("/student/<int:id>")
def student(id):
    return render_template("student.html", 
            template_name=student_data[id]["name"], 
            template_score=student_data[id]["score"])

if __name__ == '__main__':
    app.run(debug=True)