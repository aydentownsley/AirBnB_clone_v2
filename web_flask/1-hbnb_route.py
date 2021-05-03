#!/usr/bin/python3
""" simple flash web app """
from flask import Flask
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_hbnb():
    """[summary]

    Returns:
        [type]: [description]
    """
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """[summary]

    Returns:
        [type]: [description]
    """
    return ('HBNB')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
