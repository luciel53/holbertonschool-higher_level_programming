#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    d = {}
    value = 0
    for key, value in a_dictionary.items():
        d[key] = value * 2
    return d
