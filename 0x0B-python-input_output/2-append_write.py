#!/usr/bin/python3


"""module to append data to a file """


def append_write(filename="", text=""):

    """function will append data to a file """

    with open(filename, 'a', encoding='utf-8') as f:
        f.write(text)
        return len(text)
