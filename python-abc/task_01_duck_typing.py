#!/usr/bin/python3
import math

class Circle:
    """Dairə sinifi"""
    def __init__(self, radius):
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
        self.width = width
        self.height = height

    def area(self):
        """Düzbucaqlının sahəsini hesablayır"""
        return self.width * self.height

    def perimeter(self):
        """Düzbucaqlının perimetrini hesablayır"""
        return 2 * (self.width + self.height)

def shape_info(shape):
    """
    Duck typing istifadə edərək fiqur haqqında məlumat çap edir.
    Fiqurun Circle və ya Rectangle olmasının fərqi yoxdur, 
    əsas odur ki, area() və perimeter() metodları olsun.
    """
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
