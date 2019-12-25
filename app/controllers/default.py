import os
import sys
from app import app


@app.route('/index')
@app.route("/")
def index():
    return "Hello World!"


@app.route("/test/<float:obj>")
@app.route("/test/<int:obj>")
@app.route("/test/", defaults={'obj': 'visitante'})
@app.route("/test/<obj>")
def test(obj):
    tip = type(obj)
    print(type(obj))
    print(tip)
    return {
        "<class 'str'>": 'Olá %s!' % obj,
        "<class 'int'>": str(obj),
        "<class 'float'>": str(obj),
        }.get(tip, '')

