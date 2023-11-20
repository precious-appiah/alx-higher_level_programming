#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    i = 0
    try:
        for j in my_list_1:
            for k in my_list_2:
                if isinstance(j, (int, float)) or if isinstance(k, (int, float)):
                    res = j / k
                    new_list.append(res)
                    i++
                else:
                    res = 0
                    new_list.append(res)
                    i++
    except ZeroDivisionError:
        new_list.append(0)
        print("division by 0")
        i++
    except IndexError:
        new_list.append(0)
        print("out of range")
        i++
    finally:
        return new_list
