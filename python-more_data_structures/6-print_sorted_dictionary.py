#!/usr/bin/python3
"""
Module to print a dictionary by ordered keys.
"""


def print_sorted_dictionary(a_dictionary):
    """
    Prints a dictionary by ordered keys.
    """
    for key in sorted(a_dictionary.keys()):
        print(f"{key}: {a_dictionary[key]}")
