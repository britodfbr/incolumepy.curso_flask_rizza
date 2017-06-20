from app import app


@app.route("/")
def index():
    return "Página Principal"


@app.route("/hello")
def hello():
    return "Hello World!"