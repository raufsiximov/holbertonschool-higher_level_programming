#!/usr/bin/python3
"""BaseGeometry-dən törəyən Rectangle klası"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Düzbucaqlı klası"""

    def __init__(self, width, height):
        """Düzbucaqlını en və hündürlüklə inisializasiya edir"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
