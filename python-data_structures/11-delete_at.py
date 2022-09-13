#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx >= 0 and idx < len(my_list):
        for i in range(my_list[idx]):
            del my_list[idx]
    return (my_list)
