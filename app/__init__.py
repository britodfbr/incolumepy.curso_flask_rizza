import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

__version__ = '0.0.9-dev0'
template_dir = os.path.join(os.path.dirname(__file__), 'views', 'templates')
static_dir = os.path.join(os.path.dirname(__file__), 'views', 'static')

app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)
app.config.from_object('configure')
db = SQLAlchemy(app)

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

from app.controllers import default
