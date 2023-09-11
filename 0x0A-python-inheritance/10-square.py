#!/usr/bin/python3
"""Defines a Rectangle child class Square."""
Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """Type class of a square inherit a rectangle"""

    def __init__(self, size):
        """Represent a square."""

        def __init__(self, size):
            """Initialize a new square.

        Args:
            size (int): size of new square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size