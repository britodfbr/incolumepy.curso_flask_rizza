import os
import sys
from app import app


@app.route('/index')
@app.route("/")
def index():
    return "Hello World!"


@app.route("/test/", defaults={'name': 'visitante'})
@app.route("/test/<name>")
def teste(name):
    return 'Olá %s!' % name.title()
