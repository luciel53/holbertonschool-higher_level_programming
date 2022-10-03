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
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.id = id
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
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if (value) <= 0:
            raise ValueError("width must be > 0")

    @height.setter
    def height(self, value):
        self.__height = value
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if (value) <= 0:
            raise ValueError("height must be > 0")

    @x.setter
    def x(self, value):
        self.__x = value
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if (self.__x) < 0:
            raise ValueError("x must be >= 0")

    @y.setter
    def y(self, value):
        self.__y = value
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if (value) < 0:
            raise ValueError("y must be >= 0")

    def area(self):
        """
        Update the class Rectangle by adding the public method def
        area(self): that returns the area value of the Rectangle instance.
        """
        return self.__height * self.__width

    def display(self):
        """
        Update the class Rectangle by adding the public method def
        display(self): that prints in stdout the Rectangle instance with
        the character # - you don’t need to handle x and y here.
        """
        str = ((" " * self.__x + self.__width * "#" + '\n') * self.__height)
        print(str, end=""[:-1])

    def __str__(self):
        """
        Update the class Rectangle by overriding the __str__ method so
        that it returns [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """
        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(
            self.id, self.__x, self.__y, self.__width, self.__height)
