from app import app


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


@app.route('/index')
@app.route("/")
def index():
    return """
    <html>
    <head><title> Página 1 </title></head>
    Hello World!</html>"""

