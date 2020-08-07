from flask import Flask, escape, request, render_template
from jinja2 import Template, Environment, FileSystemLoader

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template("home.html")


@app.route('/about')
def about():
    return render_template('about.html')
