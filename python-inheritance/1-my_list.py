#!/usr/bin/python3
"""empty mod"""


class MyList(list):
    """a class MyList that inherits from list"""
    def print_sorted(self):
        """A function that prints the list, but sorted (ascending sort)"""
        print(sorted(self))
