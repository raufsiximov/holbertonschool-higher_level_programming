#!/usr/bin/python3
"""BaseGeometry-dən törəyən tam Rectangle klası"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Düzbucaqlı klası"""

    def __init__(self, width, height):
        """İnisializasiya və validasiya"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Düzbucaqlının sahəsini qaytarır"""
        return self.__width * self.__height

    def __str__(self):
        """Düzbucaqlı haqqında məlumatı formatlı sətir kimi qaytarır"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
