#!/usr/bin/python3
"""module"""


class Student:
    """a class Student that defines a student by"""
    def __init__(self, first_name, last_name, age):
        self.last_name = last_name
        self.first_name = first_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Public method def to_json(self): that retrieves a dictionary
        representation of a Student instance (same as 8-class_to_json.py)
        """
        d = {}
        # if no attributes, return every keys and values
        if attrs is None:
            return self.__dict__
        # else, if key is present return the value
        for key, value in self.__dict__.items():
            if key in attrs:
                d[key] = value
        return d

    def reload_from_json(self, json):
        for key, val in json.items():
            self.__dict__[key]
