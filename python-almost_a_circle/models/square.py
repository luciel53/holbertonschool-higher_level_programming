#!/usr/bin/python3
"""module"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """the class Square that inherits from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """
        Class constructor: def __init__(self, size, x=0, y=0, id=None)

        Call the super class with id, x, y, width and height - this super call
        will use the logic of the __init__ of the Rectangle class. The width
        and height must be assigned to the value of size
        You must not create new attributes for this class, use all attributes
        of Rectangle - As reminder: a Square is a Rectangle with the same
        width and height. All width, height, x and y validation must inherit
        from Rectangle - same behavior in case of wrong data
        """
        self.size = size
        super().__init__(size, size, x, y, id)


    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.size)
