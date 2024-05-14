#!/usr/bin/env python3
"""Flask App"""
from flask import Flask, render_template, request, g
from flask_babel import Babel, format_datetime
import pytz


class Config:
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)

babel = Babel(app)

@babel.localeselector
def get_locale():
    """Get Locale"""
    if request.args.get('locale', None):
        locale = request.args.get('locale')
    elif g.user:
        locale = g.user.get('locale', None)
    else:
        locale = request.headers.get('locale', None)
    if locale and locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_user(id):
    """Retrun the user from users dict"""
    users = {
        1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
        2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
        3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
        4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
    }
    return users.get(id, None)


@app.before_request
def before_request():
    """Before request"""
    id = request.args.get('login_as', None)
    if id:
        g.user = get_user(int(id))


@babel.timezoneselector
def get_timezone():
    """Get time zone"""
    timezone = request.args.get('timezone')
    if not timezone and g.user:
        timezone = g.user.get('timezone')
    try:
        return pytz.timezone(timezone).zone
    except pytz.exceptions.UnknownTimeZoneError:
        return app.config['BABEL_DEFAULT_TIMEZONE']


@app.route('/')
def home():
    """Home route"""
    return render_template('index.html', current_time=format_datetime())


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
