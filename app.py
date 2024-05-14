"""
A simple Flask application.
"""

from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    """Return a greeting message."""
    return '<h1><center>This header change was changed in a new_branch</center></h1>'


app.run(host='0.0.0.0', port=5000)
