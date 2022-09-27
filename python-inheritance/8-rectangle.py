#!/usr/bin/python3
"""empty mod"""
from calendar import c


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class BaseGeometry:
    """Write an empty class BaseGeometry"""
    def area(self):
        """
        Public instance method: def area(self): that raises an Exception
        with the message area() is not implemented
        """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """
        Public instance method: def integer_validator(self, name, value):
        that validates value
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        self.__height = height
        self.__width = width
        self.integer_validator("height", height)
        self.integer_validator("width", width)
