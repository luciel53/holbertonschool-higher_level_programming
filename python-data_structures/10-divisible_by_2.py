#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    idx = 0
    new_list = my_list.copy()
    for num in new_list:
        if num % 2 == 0:
            new_list[idx] = True
        else:
            new_list[idx] = False
        idx += 1
    return new_list
