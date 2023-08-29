#!/usr/bin/python3

from__future__ import print_function
import sys

def safe_function(fct, *args):
    try:
        result = fct(*args)
        return (result)
    except:
        print("Exception: {}".format(sys.exec_info()[1]), file=sys.stderr)
        return None
