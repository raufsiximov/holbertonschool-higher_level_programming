#!/usr/bin/python3
"""
Module to convert Roman numeral to an integer.
"""


def roman_to_int(roman_string):
    """
    Converts a Roman numeral to an integer.
    """
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    roman_map = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
    }
    total = 0

    for i in range(len(roman_string)):
        val = roman_map.get(roman_string[i], 0)
        if i + 1 < len(roman_string):
            next_val = roman_map.get(roman_string[i + 1], 0)
            if val < next_val:
                total -= val
            else:
                total += val
        else:
            total += val

    return total
