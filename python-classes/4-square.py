#!/usr/bin/python3
"""
This module defines the Square class.

The Square class has a private size attribute with controlled access
through getters and setters. It includes methods for computing the area
and printing the square using the '#' character.
"""


class Square:
    """
    Represents a square with size validation and printable shape.
    """

    def __init__(self, size=0):
        """
        Initialize a new Square.

        Args:
            size (int): Optional size of the square (default: 0).

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        self.size = size

    @property
    def size(self):
        """
        Retrieve the size of the square.

        Returns:
            int: The current size.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square with type and value validation.

        Args:
