#!/usr/bin/python3
"""
Script that starts a Flask web application:
The web application is listening on 0.0.0.0, port 5000
"""

from flask import Flask, abort
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    return "Hello HBNB!"


@app.route("/hbnb/", strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    return f'C {text.replace("_", " ")}'


@app.route("/python/", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_text(text='is cool'):
    return f'Python {text.replace("_", " ")}'


@app.route("/number/<n>", strict_slashes=False)
def is_number(n):
    try:
        int(n)
        return f'{n} is a number'
    except Exception as e:
        abort(404)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
