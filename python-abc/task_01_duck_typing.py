#!/usr/bin/python3
import math

class Circle:
    """Dairə sinifi"""
    def __init__(self, radius):
        # abs() silindi, rəqəmi olduğu kimi saxlayırıq
        self.radius = radius

    def area(self):
        """Dairənin sahəsini hesablayır"""
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """Dairənin perimetrini hesablayır"""
        return 2 * math.pi * self.radius

class Rectangle:
    """Düzbucaqlı sinifi"""
    def __init__(self, width, height):
        # abs() silindi, mənfi ölçüləri olduğu kimi qəbul edirik
        self.width = width
        self.height = height

    def area(self):
        """Düzbucaqlının sahəsini hesablayır: width * height"""
        return self.width * self.height

    def perimeter(self):
        """Düzbucaqlının perimetrini hesablayır: 2 * (width + height)"""
        return 2 * (self.width + self.height)

def shape_info(shape):
    """Duck typing istifadə edərək məlumat çap edir"""
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
