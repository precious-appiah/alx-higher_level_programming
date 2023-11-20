#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    cnt = 0
    try:
        for i in range(0, x):
            if isinstance(my_list[i], int):
                print("{:d}".format(my_list[i]), end="")
                cnt += 1
        print("")
    except IndexError:
        print("")
        print("IndexError: list index out of range")
    except Exception:
        print("")
        print("An error occured")
    return cnt
