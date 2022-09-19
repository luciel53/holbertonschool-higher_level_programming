#!/usr/bin/python3
"""This function does strictly nothing."""


class Square:
    """my first class"""
    def __init__(self, size=0):
        self.__size = size

    # getter method
    @property
    def size(self):
        return self.__size

    # property setter
    @size.setter
    def size(self, value):
        self.__size = value
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

    # public instance method
    def area(self):
        return self.__size ** 2
