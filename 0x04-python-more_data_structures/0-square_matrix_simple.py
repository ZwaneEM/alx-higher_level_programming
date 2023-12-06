#!/usr/bin/python3

def square_matrix_simple(matrix=[]):

    result_matrix = []
    for row in matrix:
        new_row = [element ** 2 for element in row]
        result_matrix.append(new_row)

    return result_matrix
