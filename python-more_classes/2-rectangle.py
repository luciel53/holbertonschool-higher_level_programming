#!/usr/bin/python3
"""Module documentation"""


class Rectangle:
    """a class Rectangle that defines a rectangle"""

    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):

        self.__width = value

        if type(value) is not int:
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):

        self.__height = value

        if type(value) is not int:
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")

    def area(self):

        if self.__width == 0 or self.__height == 0:
            perim = 0

        the_area = self.__height * self.__width
        return the_area

    def perimeter(self):
        perim = (self.__height * 2) + (self.__width * 2)
        return perim

        if self.__width == 0 or self.__height == 0:
            perim = 0
