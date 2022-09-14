#!/usr/bin/python3
from hashlib import new
from operator import ne


def uniq_add(my_list=[]):
    new_list = []
    new_list = set(my_list)
    new_list = sum(new_list)
    return new_list
