#!/usr/bin/python3
"""Rectangle klasını təyin edən modul"""


class Rectangle:
    """Eni və hündürlüyü olan bir düzbucaqlı klası"""

    def __init__(self, width=0, height=0):
        """Yeni bir Rectangle obyekti yaradır"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """width üçün getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """width üçün setter"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """height üçün getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """height üçün setter"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Düzbucaqlının sahəsini qaytarır"""
        return self.__width * self.__height

    def perimeter(self):
        """Düzbucaqlının perimetrini qaytarır"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """Düzbucaqlını # simvolu ilə təsvir edən string qaytarır"""
        if self.__width == 0 or self.__height == 0:
            return ""
        rect_str = []
        for i in range(self.__height):
            rect_str.append("#" * self.__width)
        return "\n".join(rect_str)

    def __repr__(self):
        """Obyektin kodla ifadəsini qaytarır"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Obyekt silinən zaman mesaj çap edir"""
        print("Bye rectangle...")
