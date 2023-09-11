#!/usr/bin/python3

def is_same_class(obj, a_class):
    """function to check if obj is the same class
    Arguments:
        param1: obj
        param2: a_class that matches the boj
    Return:
    True for insistance of obj or False if not
    """

    if type(obj) == a_class:
        return True
    else:
        return False