#!/usr/bin/python3
def roman_to_int(roman_string):
    d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 100}
    sum = 0
    if type(roman_string) is not str:
        return 0
    for rom in reversed(roman_string):
        numb = d[rom]
        if sum < numb * 3:
            sum += numb
        else:
            sum -= numb

    return sum
