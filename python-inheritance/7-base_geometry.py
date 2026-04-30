#!/usr/bin/python3
"""BaseGeometry klasına validator əlavə edən modul"""


class BaseGeometry:
    """Həndəsə fiqurları üçün əsas klas"""

    def area(self):
        """Sahə metodu (hələ reallaşdırılmayıb)"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Dəyərin tam ədəd və 0-dan böyük olmasını yoxlayır"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
