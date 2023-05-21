#!/usr/bin/python3


"""Flask script that displays “Hello HBNB!” """
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_world():
    """a method/function that returns hello HBNB"""
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host="0.0.0", port=5000)
