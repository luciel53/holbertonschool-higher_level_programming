#!/usr/bin/python3
divisible_by_2 = __import__('10-divisible_by_2').divisible_by_2

list = [1, 2, 3, 4]
list_result = divisible_by_2(list)

i = 0
while i < len(list):
    print("{:d} {:s} divisible by 2".format(list[i], "is" if list_result[i] else "is not"))
    i += 1
