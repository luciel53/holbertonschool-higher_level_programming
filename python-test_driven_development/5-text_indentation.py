#!/usr/bin/python3
"""
Module for a function that prints a text with 2 new lines after each of
these characters: ., ? and :
"""


def text_indentation(text):
    """
    a function that prints a text with 2 new lines after each of these
    characters: ., ? and :
    """
    c = 0

    if type(text) is not str:
        raise TypeError("text must be a string")

    while c < len(text):
        if text[c] == '.' or text[c] == '?' or text[c] == ':':
            print(text[c])
            print()
            c += 1

        else:
            print(text[c], end="")
        c += 1
