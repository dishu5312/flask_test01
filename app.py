import datetime
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html', variable="Rahul", var=	False)

@app.route('/<name1>')
def name(name1):
	now=datetime.datetime.now()
	return f'<h1>Hello! {name1}<br> {now.day} - {now.month} - {now.year}<br>{now.hour}:{now.minute}:{now.second}<br>{now} </h1>'