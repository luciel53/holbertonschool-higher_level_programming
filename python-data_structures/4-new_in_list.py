#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_list = 0
    new_list = my_list.copy()

    if idx < 0 and idx >= len(new_list):
        return None
    else:
        new_list[idx] = element
        return new_list
