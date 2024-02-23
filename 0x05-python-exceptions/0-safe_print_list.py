#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):

    tokens = 0

    try:
        while tokens < x:
            print("{}".format(my_list[tokens]), end="")
            tokens += 1

    except (IndexError, TypeError):
        pass

    print("")
    return tokens
