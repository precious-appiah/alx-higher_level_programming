#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    my_list_cp = []
    for i in range(0, len(my_list)):
        my_list_cp[i] = my_list[i]
    if idx < 0 or idx >= len(my_list):
        return my_list_cp
    my_list_cp[idx] = element
    return my_list_cp
