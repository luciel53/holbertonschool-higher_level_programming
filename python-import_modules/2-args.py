#!/usr/bin/python3
from sys import argv as av


if __name__ == "__main__":
    i = 0
    counter = len(av) - 1
    if counter == 1:
        print(counter, "argument:")
    elif counter > 1:
        print(counter, "arguments:")
    else:
        print(counter, "arguments.")

    for i in range(counter):
        print("{}: {}".format(i+1, av[i + 1]))
