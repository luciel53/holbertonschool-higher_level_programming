#!/usr/bin/python3
"""Write the first class rectangle"""
from models.base import Base


class Rectangle(Base):

    def __init__(self, width, height, x=0, y=0, id=None):

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        self.__id = id
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    def height(self):
        return self.__height

    def x(self):
        return self.__x

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
