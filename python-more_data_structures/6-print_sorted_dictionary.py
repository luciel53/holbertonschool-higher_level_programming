#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sorted_dico = sorted(a_dictionary.items())
    for key, value in sorted_dico:
        print("{} : {}".format(key, value))
