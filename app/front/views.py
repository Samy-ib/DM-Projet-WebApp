from app.front import front
from flask import render_template

@front.route('/')
def index():
    return render_template('index.html')

@front.route('/index')
def index2():
    return render_template('index2.html')