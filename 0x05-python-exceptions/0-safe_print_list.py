#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    cnt = 0
    try:
        for i in range(x):
            print(f"{my_list[i]}", end="")
            cnt += 1
    except IndexError:
        print("Not enough elemnets in list")
    except Exception:
        print("An Error occured")
    return cnt
