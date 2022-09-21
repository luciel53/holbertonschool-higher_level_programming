#!/usr/bin/python3
"""Module for a function that divides all elements of a matrix."""


def matrix_divided(matrix, div):
    """A function that divides all the elements of a matrix"""

    new_matrix = []
    row = 0
    columns = 0
    i = 0
    x = 0

    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    if type(matrix) is not list:
        if type(matrix) is not int or type(matrix) is not float:
            raise TypeError("matrix must be a matrix (list of lists) " +
                            "of integers/floats")

    for row in matrix:
        for columns in row:
            if len(row) != len(matrix[0]):
                raise TypeError("Each row of the matrix must have the " +
                                "same size")
        temp = list(map(lambda x: round(x / div, 2), row))
        new_matrix.append(temp)

    return new_matrix
