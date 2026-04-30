#!/usr/bin/python3
"""Rectangle-dan törəyən Square klası"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Kvadrat klası"""

    def __init__(self, size):
        """Kvadratı inisializasiya edir"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
