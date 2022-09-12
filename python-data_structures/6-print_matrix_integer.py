#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in range(len(matrix)):
        for c in range(len(matrix[row])):
            print("{:d} ".format(matrix[row][c]), end='')
            if c is not (len(matrix[row])):
                print(end=" ")
        print()
