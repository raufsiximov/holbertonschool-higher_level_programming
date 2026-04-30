#!/usr/bin/python3
from abc import ABC, abstractmethod

class Animal(ABC):
    """Mücərrəd baza sinifi Animal"""

    @abstractmethod
    def sound(self):
        """Mücərrəd metod, alt siniflər tərəfindən mütləq tətbiq edilməlidir"""
        pass

class Dog(Animal):
    """Animal-dan törəyən Dog sinifi"""

    def sound(self):
        """İt üçün səs metodu"""
        return "Bark"

class Cat(Animal):
    """Animal-dan törəyən Cat sinifi"""

    def sound(self):
        """Pişik üçün səs metodu"""
        return "Meow"
