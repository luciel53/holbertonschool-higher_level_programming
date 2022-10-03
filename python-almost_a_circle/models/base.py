#!/usr/bin/python3
"""Write the first class Base"""


class Base:
    """
    class constructor: def __init__(self, id=None):
    if id is not None, assign the public instance attribute id with this
    argument value - you can assume id is an integer and you don’t need to
    test the type of it otherwise, increment __nb_objects and assign the new
    value to the public instance attribute id private class attribute
    __nb_objects = 0
    """

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects