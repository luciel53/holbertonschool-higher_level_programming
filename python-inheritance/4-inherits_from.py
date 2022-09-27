#!/usr/bin/python3
"""empty mod"""


def inherits_from(obj, a_class):
    """
    a function that returns True if the object is an instance of a class
    that inherited (directly or indirectly) from the specified class ;
    otherwise False
    """
    return (type(obj) is not a_class)
