"""
A simple Flask application.
"""

from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    """Return a greeting message."""
    return '<h1><center>I changed this header again</center></h1>'


app.run(host='0.0.0.0', port=5000)
