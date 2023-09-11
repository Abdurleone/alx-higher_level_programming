#!/usr/bin/python3
"""Defines a BaseGeometry child class rectangle."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """Type class of Rectangle inherit BaseGeometry"""

    def __init__(self, width, height):
        """Intialize a new Rectangle.

        Args:
            width (int): width of new Rectangle.
            height (int): height of new Rectangle.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height