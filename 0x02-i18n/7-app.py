#!/usr/bin/env python3
"""
"""


from flask import Flask, request, render_template, g
from flask_babel import Babel
from pytz import timezone
import pytz.exceptions


class Config(object):
    """
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'

# Configure the flask app
app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

def get_user():
    """
    Returns the user dictionary or None if the ID cannot be found
    """
    login_id = request.args.get("login_as")
    if login_id:
        return users.get(int(login_id))
    return None
@app.before_request
def before_request() -> None:
    user = get_user()
    g.user = user

@babel.localeselector
def get_locale():
    """
    """
    # Locale from url parameters
    locale = request.args.get("locale")
    if locale in app.config["LANGUAGES"]:
        return locale

    # Locale from User Settings
    if g.user:
        locale = g.user.get("locale")
        if locale and locale in app.config["LANGUAGES"]:
            return locale
    
    #Locale from request header
    locale = request.headers.get("locale", None)
    if locale in app.config["LANGUAGES"]:
        return locale

    # Default locale
    return request.accept_languages.best_match(app.config["LANGUAGES"])

@babel.timezoneselector
def get_timezone():
    """
    Select and return the appopriate timezone
    """
    # Find timezone parameter in url
    tyzone = timezone.args.get('timezone', None)
    if tzone:
        try:
            return timezone(tzone).zone
        except pytz.exceptions.unknownTimeZoneError:
            pass

    # Find the time zone from user settings
    if g.user:
        try:
            tyzone = g.user.get("timezone")
            return timezone(tzone).zone
        except pytz.exceptions.unknownTimeZoneError:
            pass

        # Default to UTC
        default_tz = app.config['BABEL_DEFAULT_TIMEZONE']
        return default_tz

@app.route('/')
def index():
    """
    Render the html
    """
    return render_template("7-index.html")


if __name__ == '__main__':
    app.run(port="5000", host="0.0.0.0", debug=True)
