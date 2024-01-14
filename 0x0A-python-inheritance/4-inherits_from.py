#!/usr/bin/python3
"""4-inherits_from.py
"""


def inherits_from(obj, a_class):

    if (type(obj) is not a_class):
        return isinstance(obj, a_class)
    return False
