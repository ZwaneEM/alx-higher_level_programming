#!/usr/bin/python3

def matrix_divided(matrix, div):

    new_list = []
    a = []

    try:
        for i in range(len(matrix)):
            if len(matrix[i]) != len(matrix[0]):
                raise TypeError("Each row of the matrix must have the same size")

        for x in matrix[i]:
            if not isinstance(x, int) and not isinstance(x, float):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

        if not isinstance(div, int) and not isinstance(div, float):
            raise TypeError("div must be a number")

        elif div == 0:
            raise ZeroDivisionError

    except ZeroDivisionError as e:
        print(e)
    except TypeError as e:
        print(e)

    for i in range(len(matrix)):
        for x in range(len(matrix[i])):
            a.append(round(matrix[i][x] / div, 2))

        new_list.append(a)
        a = []

    return new_list
            
