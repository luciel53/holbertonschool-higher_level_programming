#!/usr/bin/python3
"""empty mod"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """a class Rectangle that inherits from BaseGeometry"""
    def __init__(self, width, height):
        """
        Instantiation with width and height:
        def __init__(self, width, height):
        """
        if self.__height >= 0 and self.__width >= 0:
            self.__height = height
            self.__width = width
            self.integer_validator("height", height)
            self.integer_validator("width", width)
