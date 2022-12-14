#!/usr/bin/python3
"""Module documentation"""


class Rectangle:
    """a class Rectangle that defines a rectangle"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

        the_area = self.__height * self.__width
        return the_area

    def perimeter(self):

        if self.__width == 0 or self.__height == 0:
            return 0

        perim = (self.__height * 2) + (self.__width * 2)
        return perim

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ("")
        n_str = (("#" * self.__width + '\n') * self.__height)[:-1]
        return ((str(self.print_symbol) * self.__width +
                '\n') * self.__height)[:-1]

    def __repr__(self):
        return ("Rectangle({:d}, {:d})".format(eval(repr(self.__width)), eval(
            repr(self.__height))))

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):

        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        area_1 = rect_1.area()
        area_2 = rect_2.area()

        if area_1 >= area_2:
            return rect_1

        if area_2 > area_1:
            return rect_2

    @classmethod
    def square(cls, size=0):
        return cls(height=size, width=size)
