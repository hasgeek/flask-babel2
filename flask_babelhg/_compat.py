# -*- coding: utf-8 -*-
"""
    flask.ext.babel._compat
    ~~~~~~~~~~~~~~~~~~~~~~~

    :copyright: (c) 2013 by Armin Ronacher, Daniel Neuhäuser.
    :license: BSD, see LICENSE for more details.
"""
import sys

PY2 = sys.version_info[0] == 2


if PY2:
    text_type = unicode  # NOQA: F821
    string_types = (str, unicode)  # NOQA: F821
else:
    text_type = str
    string_types = (str,)
