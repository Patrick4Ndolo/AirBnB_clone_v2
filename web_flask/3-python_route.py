#!/usr/bin/python3

"""
Flask web App
"""
from flask import Flask
app = Flask("__name__")


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    hello_hbnb: displays return value
    """
    return 'Hello, HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    hbnb: displays hbnb
    """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    """
    c_is_fun: replaces _ with " " and displays kwags
    """
    return "C " + text.replace("_", " ")


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_is_cool(text='is_cool'):
    """
    python_is_cool: replaces _  with " " and displays kwags
    """
    return "Python " + text.replace("_", " ")


if (__name__) == "__main__":
    """
    main function
    """
    app.run(host='0.0.0.0', port=5000)
