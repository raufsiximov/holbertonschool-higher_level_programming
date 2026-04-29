#!/usr/bin/python3
"""
Module to convert Roman numeral to an integer.
"""


def roman_to_int(roman_string):
    """
    Converts a Roman numeral to an integer.
    """
    if type(roman_string) is not str or roman_string is None:
        return 0

    roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0

    for i in range(len(roman_string)):
        if (i + 1 < len(roman_string) and
                roman_map[roman_string[i]] < roman_map[roman_string[i + 1]]):
            total -= roman_map[roman_string[i]]
        else:
            total += roman_map[roman_string[i]]

    return total
