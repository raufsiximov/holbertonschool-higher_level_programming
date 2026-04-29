#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(list_length):
        res = 0
        try:
            # Siyahı elementlərinin tipini yoxlayırıq
            if not isinstance(my_list_1[i], (int, float)) or \
               not isinstance(my_list_2[i], (int, float)):
                print("wrong type")
                res = 0
            else:
                res = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
            res = 0
        except IndexError:
            print("out of range")
            res = 0
        finally:
            new_list.append(res)
    return new_list
