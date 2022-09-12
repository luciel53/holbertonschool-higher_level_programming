#!/usr/bin/python3
def no_c(my_string):
    translation = {67: None, 99: None}
    for i in range(len(my_string)):
        if my_string[i] is not None:
            new_string = my_string.translate(translation)
    return new_string
