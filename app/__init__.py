import os
from flask import Flask

# template_dir = os.path.join(os.path.dirname(__file__), 'views', 'templates')
# static_dir = os.path.join(os.path.dirname(__file__), 'views', 'static')

# app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)
__version__ = '0.0.1-dev0'
app = Flask(__name__)

from app.controllers import default
