#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):

    n1 = tuple_a + ('0', '0')
    n2 = tuple_b + ('0', '0')

    result_1 = int(n1[0]) + int(n2[0])
    result_2 = int(n1[1]) + int(n2[1])

    return (result_1, result_2)
