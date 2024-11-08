#!/usr/bin/env python3
"""
Simple Flask app
"""


from flask import Flask, render_template, request
from flask_babel import Babel


class Config(object):
    """

    Returns:
            _type_: _description_
    """
    LANGUAGES = ['en', 'fre']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


# Configure the flask app
app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


@babel.localeselector
def get_locale():
    """
    _summary_

    Returns:
            _type_: _description_
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """summary
    """
    return render_template('3-index.html')


if __name__ == "__main__":
    app.run(port="5000", host="0.0.0.0", debug=True)
