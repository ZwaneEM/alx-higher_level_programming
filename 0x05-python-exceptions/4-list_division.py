#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    i = 0

    while i < list_length:
        try:
            if isinstance(my_list_1[i], str) or isinstance(my_list_2[i], str):
                raise TypeError("wrong type")

            if my_list_2[i] == 0:
                raise ZeroDivisionError("division by zero")

            result = my_list_1[i] / my_list_2[i]
            new_list.append(result)

        except (TypeError, ZeroDivisionError) as e:
            print(e)
            new_list.append(0)

        except IndexError:
            print("out of range")
            new_list.append(0)

        finally:
            i += 1

    return new_list
