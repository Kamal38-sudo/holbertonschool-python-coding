#!/usr/bin/python3
"""
This module defines the Square class.
"""
class Square:
    """
    This class defines a square by
    a private instance attribute: size.
    """
    def __init__(self, size):
        """
        Initialize a new Square.
        Args:
            size: The size of the square (no type/value validation required).
        """
        self.__size = size
