#!/usr/bin/env python3
""" a script that starts a Basic Babel setup """

from flask import request, Flask, render_template
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config(object):
    '''Babel config'''
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object('4-app.Config')


@app.route('/', methods=['GET'], strict_slashes=False)
def hello() -> str:
    ''' returns a simple page '''
    return render_template('4-index.html')


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


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
