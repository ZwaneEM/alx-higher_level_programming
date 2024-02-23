#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):

    tokens = 0

    try:
        for i in range(x):
            if isinstance(my_list[i], int):
                print("{:d}".format(my_list[i]), end="")
                tokens += 1

            else:
                continue

    except TypeError:
        pass

    print("")
    return tokens
