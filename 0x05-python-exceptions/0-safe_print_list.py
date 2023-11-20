#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    cnt = 0
    try:
        for i in range(x):
            print(f"{my_list[i]}", end="")
            cnt += 1
        print("")
    except IndexError:
        print("")
        return cnt
    except Exception:
        print("An Error occured")
    return cnt
