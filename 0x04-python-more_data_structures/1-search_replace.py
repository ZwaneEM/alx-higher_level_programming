#!/usr/bin/python3

def search_replace(my_list, search, replace):
    count = my_list.count(search)
    new_list = []

    if count > 0:
        for i in my_list:
            new_list.append(i)

        for v in range(count):
            index = new_list.index(search)
            new_list[index] = replace

        return new_list

    return my_list
