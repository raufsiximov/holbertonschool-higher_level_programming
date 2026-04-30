#!/usr/bin/python3
import math

class Circle:
    def __init__(self, radius):
        # Circle üçün mənfini müsbətə çeviririk (Test belə tələb edir)
        self.radius = abs(radius)

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius

class Rectangle:
    def __init__(self, width, height):
        # Rectangle üçün abs() İSTİFADƏ ETMİRİK (Test mənfi cavab gözləyir)
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

def shape_info(shape):
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
