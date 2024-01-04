#!/usr/bin/python3
"""
Script that starts a Flask web application:
The web application is listening on 0.0.0.0, port 5000
"""

from flask import Flask, abort, render_template
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


@app.route("/number_template/<n>", strict_slashes=False)
def number_template(n):
    try:
        number = int(n)
        return render_template('5-number.html', number=number)
    except Exception as e:
        abort(404)


@app.route("/number_odd_or_even/<n>", strict_slashes=False)
def number_odd_or_even(n):
    try:
        if int(n) % 2 == 0:
            text = 'even'
        else:
            text = 'odd'
        return render_template('6-number_odd_or_even.html', n=n, text=text)
    except Exception as e:
        abort(404)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
