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
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.size)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, size):
        self.width = size

    def update(self, *args, **kwargs):
        """
        Update the class Square by adding the public method def
        update(self, *args, **kwargs) that assigns attributes:

        *args is the list of arguments - no-keyworded arguments
            1st argument should be the id attribute
            2nd argument should be the size attribute
            3rd argument should be the x attribute
            4th argument should be the y attribute
        **kwargs can be thought of as a double pointer to a dictionary:
        key/value (keyworded arguments)
        **kwargs must be skipped if *args exists and is not empty
        Each key in this dictionary represents an attribute to the instance
        """
        i = 0

        if args:
            for arg in args:
                if i == 0:
                    self.id = arg

                if i == 1:
                    self.size = arg

                if i == 2:
                    self.x = arg

                if i == 3:
                    self.y = arg
                i += 1

        for key, value in kwargs.items():
            setattr(self, key, value)
