#!/usr/bin/python3
"""Write the first class rectangle"""
from models.base import Base


class Rectangle(Base):
    """Class Rectangle inherits from Base
    Private instance attributes, each with its own public getter and setter:

    __width -> width
    __height -> height
    __x -> x
    __y -> y
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """Class constructor: def __init__(self, width, height, x=0, y=0,
        id=None):
        Call the super class with id - this super call with use the logic of
        the __init__ of the Base class
        Assign each argument width, height, x and y to the right attribute
        """
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        self.__id = id
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @property
    def x(self):
        return self.__x
        
    @property
    def y(self):
        return self.__y

    @width.setter
    def width(self, value):
        self.__width = value

    def height(self):
        return self.__height

    def x(self):
        return self.__x

    def y(self):
        return self.__y
