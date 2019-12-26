from flask import render_template
from app import app
from app.models.login import LoginForm


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


@app.route('/index/<user>')
@app.route("/index/", defaults={'user': None})
@app.route("/", defaults={'user': None})
def index(user):
    return render_template("new_index.html", user=user)


@app.route('/login')
def login():
    login_form = LoginForm()
    return render_template("login.html", form=login_form)
