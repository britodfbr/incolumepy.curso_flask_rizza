from app import app
from flask import render_template

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

@app.route('/h1')
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
@app.route("/", defaults={'user':None})
def index(user):
    return render_template('hello.html', user=user)