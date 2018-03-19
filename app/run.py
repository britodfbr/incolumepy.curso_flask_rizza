import os
import sys
try:
    from app import app
except ImportError:
    sys.path.append(os.path.abspath('../'))
    print(os.path.abspath('../'))
    from app import app

if __name__ == '__main__':
    app.run()