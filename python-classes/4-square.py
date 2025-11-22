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
            value (int): New size value.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is negative.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """
        Compute and return the area of the square.

        Returns:
            int: Area of the square (size × size).
        """
        return self.__size * self.__size

    def my_print(self):
        """
        Print the square in stdout using '#' characters.

        If size is 0, prints an empty line.
        """
        if self.__size == 0:
            print("")
            return

        for _ in range(self.__size):
            print("#" * self.__size)

