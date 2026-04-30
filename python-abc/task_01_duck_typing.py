#!/usr/bin/python3
import math

class Circle:
    """Dairə sinifi"""
    def __init__(self, radius):
        # Mənfi radius daxil edilərsə, mütləq qiymətini götürürük
        self.radius = abs(radius)

    def area(self):
        """Dairənin sahəsini hesablayır"""
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """Dairənin perimetrini hesablayır"""
        return 2 * math.pi * self.radius

class Rectangle:
    """Düzbucaqlı sinifi"""
    def __init__(self, width, height):
        # Ölçülərin mütləq qiymətini götürürük
        self.width = abs(width)
        self.height = abs(height)

    def area(self):
        """Düzbucaqlının sahəsini hesablayır"""
        return self.width * self.height

    def perimeter(self):
        """Düzbucaqlının perimetrini hesablayır"""
        return 2 * (self.width + self.height)

def shape_info(shape):
    """Duck typing istifadə edərək məlumat çap edir"""
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
