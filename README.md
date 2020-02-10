# Flask Babelhg - 0.12.3

[![Build Status](https://travis-ci.org/hasgeek/flask-babelhg.svg?branch=master)](https://travis-ci.org/hasgeek/flask-babelhg)
![license](https://img.shields.io/github/license/hasgeek/flask-babelhg.svg?maxAge=2592000)

Implements i18n and l10n support for Flask. This is based on the Python
[babel][] module as well as [pytz][] both of which are installed automatically
for you if you install this library.

This release merges additional functionality from Flask-BabelEx:

1. It is possible to use multiple language catalogs in one Flask application;
2. Localization domains: your extension can package localization file(s) and use them
   if necessary;
3. Does not reload localizations for each request.

Flask-Babelhg is API-compatible with Flask-Babel.


# Documention

The latest documentation is available [here][docs].

[babel]: https://github.com/python-babel/babel
[pytz]: https://pypi.python.org/pypi/pytz/
[docs]: https://pythonhosted.org/Flask-Babelhg/
