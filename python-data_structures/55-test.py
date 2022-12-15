#!/usr/bin/python3
def no_c(my_string):
    str = ''
    for c in my_string:
        if c != chr(99) and c != chr(67):
            print(c, end='')
    return str
