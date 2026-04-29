#!/usr/bin/python3
"""
This module contains a function that computes
the square value of all integers of a matrix.
"""


def square_matrix_simple(matrix=[]):
    """
    Computes the square value of all integers of a matrix.
    Args:
        matrix: A 2D list of integers.
    Returns:
        A new matrix with squared values.
    """
    return [[i**2 for i in row] for row in matrix]
