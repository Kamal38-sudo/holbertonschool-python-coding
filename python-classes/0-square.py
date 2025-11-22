#!/usr/bin/python3
"""
This module defines the Square class.

The Square class has a private instance attribute 'size'.
"""


class Square:
    """
    Represents a square.

    Attributes:
        __size (int): The size of the square (private).
    """

    def __init__(self, size):
        """
        Initialize the square with a given size.

        Args:
            size: The size of the square (no type/value checks required).
        """
        self.__size = size

