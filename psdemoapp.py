from flask import Flask
from time import ctime
from os import environ

app = Flask(__name__)


@app.route('/ts')
def ts():
    """http://127.0.0.1:5000/ts"""
    return f'<h1>Current timestamp: {ctime()}</h1>'


@app.route('/env')
def env():
    """http://127.0.0.1:5000/env"""
    content = ''
    for name, value in environ.items():
        content += f'<tr><td>{name}</td><td>{value}</td></tr>'

    return f'<table cellspacing="5" cellpadding="5">{content}</table>'


if __name__ == '__main__':
    app.run(debug=True)
