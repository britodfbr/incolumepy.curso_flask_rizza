import os
import sys
from app import app


@app.route('/index')
@app.route("/")
def index():
    return "Hello World!"


@app.route("/test/<float:obj>")
@app.route("/test/<int:obj>")
@app.route("/test/<obj>")
@app.route("/test/", defaults={'obj': 'visitante'})
def test(obj):
    tip = str(type(obj))
    print(tip)
    return {
        "<class 'int'>": str(obj),
        "<class 'float'>": str(obj),
        "<class 'str'>": 'Olá %s!' % obj.title(),
    }.get(tip, '')
