#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    """
    A function that deletes a key in a dictionary
    with all values multiplied by 2
    """
    new_dict = {}
    for key, value in a_dictionary.items():
        new_dict.update({key: (value * 2)})
    return new_dict
