#!/usr/bin/env python3
""" Basic Flask app """
from flask import Flask, request
from flask import render_template
from flask_babel import Babel

app = Flask(__name__)


""" Instantiate Babel object"""
babel = Babel(app)


class Config:
    """ Config class with LANGUAGES, default locale, and timezone"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


""" Use Config as config for Flask app"""
app.config.from_object(Config)


""" Define get_locale function"""
@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def index() -> str:
    """
    Renders a basic html template
    """
    return render_template('3-index.html')


if __name__ == '__main__':
    app.run()
