#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        for i in range(x):
            if type(my_list[i]) in [int, float]:
                print("{}".format(my_list[i]), end="")
            else:
                continue
    except IndexError:
        print("Not enough elemnets in list")
    except Exception:
        print("An Error occured")
