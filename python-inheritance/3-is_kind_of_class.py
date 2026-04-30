#!/usr/bin/python3
"""Module that checks if an object is an instance of a class."""


def is_kind_of_class(obj, a_class):
    """Checks if obj is an instance of, or inherited from, a_class."""
    return isinstance(obj, a_class)
