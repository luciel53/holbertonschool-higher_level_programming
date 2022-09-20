#!/usr/bin/python3
"""Module for a function that adds 2 integers"""


def add_integer(a, b=98):
    """This function adds 2 integers if float and int or raise an error"""

    if a is None or type(a) is not float and type(a) is not int:
        raise TypeError("a must be an integer")

    if type(b) is not float and type(b) is not int:
        raise TypeError("b must be an integer")

    return int(a) + int(b)
