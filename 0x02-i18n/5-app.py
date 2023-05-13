#!/usr/bin/env python3
""" a script that starts a Basic Babel setup """

from flask import request, Flask, render_template, g
from flask_babel import Babel
from typing import Union

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

app = Flask(__name__)
babel = Babel(app)


class Config(object):
    '''Babel config'''
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object('5-app.Config')


@app.route('/', methods=['GET'], strict_slashes=False)
def hello() -> str:
    ''' returns a simple page '''
    return render_template('5-index.html')


@babel.localeselector
def get_locale() -> str:
    '''determine the best match for supported languages
       detect if the incoming request contains locale
    '''
    if request.args.get('locale'):
        locale = request.args.get('locale')
        if locale in app.config['LANGUAGES']:
            return locale
    else:
        return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_user() -> Union[dict, None]:
    '''returns a user dictionary or None'''
    if request.args.get('login_as'):
        user = int(request.args.get('login_as'))
        if user in users:
            return users.get(user)
    else:
        return None


@app.before_request
def before_request():
    '''to find a user if any'''
    g.user = get_user()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
