#!/usr/bin/python3
"""Eyni klas olub olmadığını yoxlayan funksiya"""


def is_same_class(obj, a_class):
    """Obyektin dəqiq verilmiş klasın nümunəsi olub olmadığını qaytarır"""
    return type(obj) is a_class
