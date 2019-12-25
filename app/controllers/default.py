import os
import sys
from app import app


@app.route('/index')
@app.route("/")
def index():
    return "Hello World!"


@app.route("/test/", defaults={'name': None})
@app.route("/test/<name>")
def teste(name):
    if name:
        return 'Olá %s!' % name
    else:
        return "Olá visitante!"
