#!/usr/bin/python3
"""Defines a class MyInt inheriting from int."""

class MyInt(int):
    """Type class of MyInt inherit int type"""

    def __eq__(self, other):
        """Override == opeartor with != behavior."""
        return self.real !=other

    def __ne__(self, other):
        """Override != opeartor with == behavior."""
        return self.real == other