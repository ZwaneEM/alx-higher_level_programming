#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):

    for i in range(len(matrix)):
        for s in range(len(matrix[i])):
            print("{:d}".format(matrix[i][s]), end=" ")

        print("")
