#!/usr/bin/python3


""" module to open file and writhe content to stdout"""


def read_file(filename=""):

    """  function that reads file an write to output"""

    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    print("{}".format(content), end ='')
