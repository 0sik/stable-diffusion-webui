from flask import Flask, Blueprint,render_template
import db_connect
motionai = Blueprint('/motionai', __name__)
@motionai.route('/motionai') 
def motionaifun():
    return render_template('motionai.html')
