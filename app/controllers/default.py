import os
import sys
from app import app


@app.route('/index')
@app.route("/")
def index():
    return "Hello World!"


@app.route("/test/", defaults={'name': 'visitante'})
@app.route("/test/<name>")
def test(name):
    return 'Olá %s!' % name.title()


@app.route("/test/<int:oid>")
def test2(oid):
    print(type(oid))
    return str(oid)


@app.route("/test/<float:oid>")
def test3(oid):
    print(type(oid))
    return str(oid)
