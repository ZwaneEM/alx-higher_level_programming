#!/usr/bin/python3

def uniq_add(my_list=[]):

    list_set = set(my_list)
    sum_r = 0

    for i in list_set:
        sum_r += i

    return sum_r
