#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    i = 0
    try:
        for j, k in zip(my_list_1, my_list_2):
            try:
                if isinstance(j, (int, float)) and  isinstance(k, (int, float)):
                    res = j / k
                    new_list.append(res)
                else:
                    res = 0
                    new_list.append(res)
                    i++
            except ZeroDivisionError:
                new_list.append(0)
                print("division by 0")
            except IndexError:
                new_list.append(0)
                print("out of range")
    except Exception as err:
        print("Exception {}".format(err))
    finally:
        return new_list
