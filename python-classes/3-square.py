#!/usr/bin/python3
"""
This module defines the Square class.

The Square class represents a geometric square with a private
size attribute that is controlled using property getters and
setters. It includes validation to ensure the size is always
a non-negative integer and provides a method to compute the
area of the square.
"""


class Square:
    """
    Represents a square with a validated size attribute.

    Attributes:
        __size (int): The length of a side of the square (private).
    """

    def __init__(self, size=0):
        """
        Initialize a new Square instance.

        Args:
            size (int): The initial size of the square (default: 0).

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is negative.
        """
        self.size = size

    @property
    def size(self):
        """
        Retrieve the current size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square with validation.

        Args:
            value (int): The new size value to set.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is negative.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """
        Calculate the area of the square.

        Returns:
            int: The computed area (size × size).
        """
        return self.__size * self.__size

