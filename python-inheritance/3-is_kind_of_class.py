#!/usr/bin/python3
"""Eyni klas və ya ondan törəmiş klas olub olmadığını yoxlayan funksiya"""


def is_kind_of_class(obj, a_class):
    """Obyektin verilmiş klasın və ya ondan törəmiş klasın nümunəsi olub olmadığını yoxlayır"""
    return isinstance(obj, a_class)
