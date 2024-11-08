#!/usr/bin/env python3
"""
Create a get_locale function with the
babel.localeselector decorator. Use
request.accept_languages to determine
the best match with our supported languages.
"""


from flask import Flask, render_template, request
from flask_babel import Babel


class Config(object):
    """
    Config Class
    """

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = "UTC"


# Configure the Flask app
app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """
    Locale function
    """

    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route("/")
def index():
    """
    render template
    """

    return render_template('2-index.html')


if __name__ == "__main__":
    app.run(port="5000", host="0.0.0.0", debug=True)
