#!/usr/bin/python3
""" simple flash web app """
from flask import Flask, render_template, escape
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


@app.route('/c/<text>')
def c_text(text):
    """[summary]

    Args:
        text ([type]): [description]

    Returns:
        [type]: [description]
    """
    if text:
        if '_' in text:
            text = text.replace("_", " ")
    return 'C {}'.format(escape(text))


@app.route('/python')
@app.route('/python/<text>')
def python_return(text='is cool'):
    """[summary]

    Args:
        text (str, optional): [description]. Defaults to 'is cool'.

    Returns:
        [type]: [description]
    """
    if not text:
        text = 'is cool'
    if '_' in text:
        text = text.replace("_", " ")
    return 'Python {}'.format(escape(text))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
