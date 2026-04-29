#!/usr/bin/python3
"""
Module to square a matrix.
"""


def square_matrix_simple(matrix=[]):
    """
    Computes the square value of all integers of a matrix.
    """
    return [[i**2 for i in row] for row in matrix]
