#!/usr/bin/python3
"""This module defines a Square class with size validation, area, and print methods."""


class Square:
    """Class that defines a square with private size and printing capabilities."""

    def __init__(self, size=0):
        """Initialize the square with optional size.

        Args:
            size (int): size of the square (default 0)

        Raises:
            TypeError: if size is not an integer
            ValueError: if size < 0
        """
        self.size = size  # use setter for validation

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square with validation.

        Args:
            value (int): new size of the square

        Raises:
            TypeError: if value is not an integer
            ValueError: if value < 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current square area."""
        return self.__size * self.__size

    def my_print(self):
        """Print the square using the '#' character."""
        if self.__size == 0:
            print()
            return

        for _ in range(self.__size):
            print("#" * self.__size)

