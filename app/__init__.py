import os
import sys
from flask import Flask

sys.path.append(os.path.abspath('../'))
#print(sys.path)
app = Flask(__name__)

from app.controllers import default