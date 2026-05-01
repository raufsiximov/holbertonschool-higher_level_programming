#!/usr/bin/python3
"""Student klassını diskdən yükləmə metodu ilə təyin edən modul."""


class Student:
    """Tələbə məlumatlarını saxlayan klass."""

    def __init__(self, first_name, last_name, age):
        """İnisializasiya metodu."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Obyektin lüğət təsvirini qaytarır."""
        if isinstance(attrs, list) and all(isinstance(x, str) for x in attrs):
            return {k: v for k, v in self.__dict__.items() if k in attrs}
        return self.__dict__

    def reload_from_json(self, json_data):
        """Lüğətdəki məlumatlarla bütün atributları yeniləyir."""
        for key, value in json_data.items():
            setattr(self, key, value)
