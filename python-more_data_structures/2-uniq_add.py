#!/usr/bin/python3
"""
Module to add unique integers in a list.
"""


def uniq_add(my_list=[]):
    """
    Adds all unique integers in a list.
    """
    return sum(set(my_list))
