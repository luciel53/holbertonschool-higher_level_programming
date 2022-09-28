#!/usr/bin/python3
"""Import doc"""
Square = __import__('10-square').Square
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    a class Square that inherits from Rectangle (9-rectangle.py).
    (task based on 10-square.py).
    """
    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        return str("[Square] {}/{}".format(self.__size, self.__size))

    def area(self):
        return self.__size ** 2
