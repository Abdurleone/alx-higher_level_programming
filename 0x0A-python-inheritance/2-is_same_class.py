#!/usr/bin/python3
"""Defines a function to confirm class."""

def is_same_class(obj, a_class):
    """Confirm an object is an instance of a given class.
    Args:
        obj (any): Object to check.
        a_class (type): Class to mstch type of obj to.
    Returns:
    True for insistance of obj or False if not
    """

    if type(obj) == a_class:
        return True
    return False
