#!/usr/bin/python3
""" simple flash web app """
from flask import Flask, render_template, escape
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_hbnb():
    """
    Returns: Hello HBNB!
    """
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """
    Returns: HBNB
    """
    return ('HBNB')


@app.route('/c/<text>')
def c_text(text):
    """ Prints string from url

    Args:
        text ([type]): [description]
    """
    if text:
        if '_' in text:
            text = text.replace("_", " ")
    return 'C {}'.format(escape(text))


@app.route('/python')
@app.route('/python/<text>')
def python_return(text='is cool'):
    """ Prints string using url

    Args:
        text (str, optional): [description]. Defaults to 'is cool'.
    """
    if '_' in text:
        text = text.replace("_", " ")
    return 'Python {}'.format(escape(text))


@app.route('/number/<int:n>')
def is_num(n):
    """ displays only if number is int

    Args:
        n: input
    """
    return '{} is a number'.format(n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
