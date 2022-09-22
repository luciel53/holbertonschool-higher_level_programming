#!/usr/bin/python3
"""Module documentation"""


class Rectangle:
    """a class Rectangle that defines a rectangle"""

    def __init__(self, width=0, height=0):
        self.__height = height
        self.__width = width

    @property
    def width(self):
        return self.width

    @width.setter
    def width(self, value):
        self.__width = value

        if type(self.__width) is not int:
            raise TypeError("width must be an integer")

        elif self.__width < 0:
            raise ValueError("width must be >= 0")

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

        if type(self.__height) is not int:
            raise TypeError("height must be an integer")

        elif self.__height < 0:
            raise ValueError("height must be >= 0")
