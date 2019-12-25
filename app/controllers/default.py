import os
import sys
from app import app


@app.route('/index')
@app.route("/")
def index():
    return "Hello World!"


@app.route("/teste")
def teste():
    return 'Olá!'
