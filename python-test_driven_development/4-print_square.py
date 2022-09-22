#!/usr/bin/python3
"""Module for a function that prints a square with the character #."""


def print_square(size):
    """a function that prints a square with the character #."""
    row = 0
    columns = 0

    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    if type(size) is not int:
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for row in range(size):
        for col in range(size):
            print("#", end="")
        print()
