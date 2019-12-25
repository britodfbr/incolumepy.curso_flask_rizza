import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

template_dir = os.path.join(os.path.dirname(__file__), 'views', 'templates')
static_dir = os.path.join(os.path.dirname(__file__), 'views', 'static')

app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////storage.db'
db = SQLAlchemy(app)
__version__ = '0.0.2-dev0'

from app.controllers import default
