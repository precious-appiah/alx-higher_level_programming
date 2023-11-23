#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    try:
        for i in range(list_length):
            j = my_list_1[i] if i < len(my_list_1) else None
            k = my_list_2[i] if i < len(my_list_2) else None

            if (j is not None and k is None) or (k is not None and j is None):
                new_list.append(0)
                print("out of range")
            else:
                if isinstance(j, (int, float)) and isinstance(k, (int, float)):
                    if k == 0:
                        new_list.append(0)
                        print("division by 0")
                    else:
                        res = j / k
                        new_list.append(res)
                else:
                    res = 0
                    print("wrong type")
                    new_list.append(res)
    except Exception as err:
        print("Exception {}".format(err))
    finally:
        return new_list
