import os
import sys
from app import app


@app.route('/index')
@app.route("/")
def index():
    return "Hello World!"


@app.route("/test/<float:obj>")
@app.route("/test/<int:obj>", methods=['GET'])
@app.route("/test/<obj>", methods=['GET'])
@app.route("/test/", defaults={'obj': 'visitante'})
def test(obj):
    t = str(type(obj))
    print(t)
    return {
        "<class 'int'>": 'int: %s.' % obj,
        "<class 'float'>": 'float: %s.' % obj,
        "<class 'str'>": 'Olá %s!' % obj.title() if isinstance(obj, str) else obj,
    }.get(t, 'Ops..')

