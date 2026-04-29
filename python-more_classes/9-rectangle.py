#!/usr/bin/python3
"""Rectangle klasını təyin edən modul"""


class Rectangle:
    """Eni, hündürlüyü və kvadrat yaratma metodu olan düzbucaqlı klası"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Yeni obyekt yaradır və sayğacı artırır"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Sahəsi böyük olan düzbucaqlını qaytarır"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """Eni və hündürlüyü size-a bərabər olan yeni Rectangle qaytarır"""
        return cls(size, size)

    def __str__(self):
        """Düzbucaqlını print_symbol ilə çəkir"""
        if self.__width == 0 or self.__height == 0:
            return ""
        rect_str = []
        for i in range(self.__height):
            rect_str.append(str(self.print_symbol) * self.__width)
        return "\n".join(rect_str)

    def __repr__(self):
        """Obyektin rəsmi təsvirini qaytarır"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Obyekt silinəndə mesaj çap edir və sayğacı azaldır"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
