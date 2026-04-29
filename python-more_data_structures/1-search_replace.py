#!/usr/bin/python3
"""
Module to replace all occurrences of an element by another in a new list.
"""


def search_replace(my_list, search, replace):
    """
    Replaces all occurrences of an element by another in a new list.
    """
    return [replace if i == search else i for i in my_list]
