#!/usr/bin/python3
"""Rectangle-dan törəyən təkmilləşdirilmiş Square klası"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Kvadrat klası"""

    def __init__(self, size):
        """Kvadratı inisializasiya edir"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """Kvadrat haqqında məlumatı [Square] formatında qaytarır"""
        return "[Square] {}/{}".format(self.__size, self.__size)
