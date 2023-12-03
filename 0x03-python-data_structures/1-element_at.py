#!/usr/bin/python3

def element_at(my_list, idx):
    leng = len(my_list)

    if idx < 0 or idx >= leng:
        return None

    return my_list[idx]
