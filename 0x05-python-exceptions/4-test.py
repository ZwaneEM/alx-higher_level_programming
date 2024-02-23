#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):

    new_list = list()
    i, x = 0, 0

    while i < list_length:

        try:

            print("i is {} and x is {}".format(i, x))
            if isinstance(my_list_1[i], str):
                new_list.append(0)
                i += 1
                raise TypeError


            if isinstance(my_list_2[x], str):
                new_list.append(0)
                x += 1
                raise TypeError

            if my_list_2[x] > my_list_1[i]:
                new_list.append(0)
            else:
                new_list.append(my_list_1[i] / my_list_2[x])
            i += 1
            x += 1

        except TypeError:
            print("wrong type")
            new_list.append(my_list_1[i] / my_list_2[x])

        except ZeroDivisionError as errzero:
            new_list.append(0)
            i += 1
            x += 1
            print(errzero)

        except IndexError:
            print("out of range")
            return new_list

    return new_list
