#!/usr/bin/python3
from hashlib import new


def divisible_by_2(my_list=[]):
    i = 0
    new_list = my_list.copy()
    for i in new_list:
        if i % 2 == 0:
            new_list[i] = True
        else:
            new_list[i] = False
    return new_list
