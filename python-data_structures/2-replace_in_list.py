#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    my_new_list = 0
    if idx >= 0 and idx < len(my_list):
        my_list[idx] = element
        return my_list
    else:
        return my_list
