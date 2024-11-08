#!/usr/bin/env python3
"""
Instantiating the Babel App
"""


from flask import Flask, render_template
from flask_babel import Babel

class Config(object):
    """
    Configuration Class for setting up the Flask App
    """

    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'

#Configure the flask app
app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)

@app.route('/')
def index():
    """
    __summary__
    """
    return render_template("1-index.html")


if __name__ == "__main__":
    app.run(port="5000", host="0.0.0.0", debug = True)
