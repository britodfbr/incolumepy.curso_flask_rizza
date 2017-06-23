from app import app

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

@app.route('/index')
@app.route("/")
def index():
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