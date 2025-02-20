#!/usr/bin/python3
''' script that starts a Flask web application. '''
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_world():
    ''' print  Hello HBNB'''
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hello_hbnb():
    ''' print  Hello HBNB'''
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def hello_text(text):
    ''' print  text and replace underscore'''
    new_text = text.replace("_", " ")
    return 'C {}'.format(new_text)


if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')
