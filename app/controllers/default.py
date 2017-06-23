from app import app
from flask import render_template
from app.models.forms import LoginForm

@app.route("/hello")
def hello():
    return "Hello World!"

@app.route('/teste', defaults={'name': None})
@app.route('/teste/<name>')
def teste(name):
    if name:
        return 'Olá, %s!' % name
    else:
        return 'Olá usuário!'

@app.route('/html')
def hi():
    return '''
        <html>
        <head>
           <title> Hello World </title>
        </head>
        <body>
        <h1> Hello World! </h1>
        </body>
        </html>
        '''

@app.route('/index/<user>')
@app.route('/index', defaults={'user':None})
@app.route("/", defaults={'user':None})
def index(user):
    return render_template('index.html',
                           user=user)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html',
                           form=form)