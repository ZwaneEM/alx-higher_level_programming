#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):

    new_tuple = ()
    first_set = [0, 0]
    second_set = [0, 0]

    for i in range(len(tuple_a)):
        first_set[i] = tuple_a[i]

    for v in range(len(tuple_b)):
        second_set[v] = tuple_b[v]

    new_tuple = first_set[0] + second_set[0], first_set[1] + second_set[1]
    return new_tuple
