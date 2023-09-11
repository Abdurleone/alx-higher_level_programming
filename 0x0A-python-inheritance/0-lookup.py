#!/usr/bin/python3
"""Defines a function to look for methods & attributes."""

def lookup(obj):
    """Return list of atributes and methods."""
    return (dir(obj))
