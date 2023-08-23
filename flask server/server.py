from flask import Flask
from dataviewer.viewer import dataviewer
from motionai.motion import motionai
app = Flask(__name__)

app.register_blueprint(dataviewer)
app.register_blueprint(motionai)

if __name__ == '__main__':
    app.run(debug=True)

# 여기서 app.run(192.168.0.51)
# 포트번호 입력하면 이대로 됨