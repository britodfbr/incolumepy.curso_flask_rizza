import os
import sys
try:
    from app import app
except ImportError:
    sys.path.append(os.path.abspath('../'))



@app.route("/")
def index():
    return "Hello World!"