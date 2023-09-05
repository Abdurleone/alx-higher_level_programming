#!/usr/bin/python3
"""Defines a square-printing function."""

def print_square(size):
    """Print a sqaure with the # character.

    Args:
        size (int): The height/width of the square.
    Raises:
        TypeError: If size is not an integer.
        ValueError: if size is < 0
    """
    If not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must ne >= 0")

    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")