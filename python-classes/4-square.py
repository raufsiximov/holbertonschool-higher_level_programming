#!/usr/bin/python3
"""
Module that defines a Square class with property getter and setter.
"""


class Square:
    """
    Represents a square with private size attribute.
    """

    def __init__(self, size=0):
        """
        Initializes the square with a size.
        Args:
            size (int): The size of the square.
        """
        self.size = size

    @property
    def size(self):
        """Retrieves the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the current area of the square."""
        return self.__size ** 2
