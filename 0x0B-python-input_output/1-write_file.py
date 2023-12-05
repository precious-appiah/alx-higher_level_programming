#!/usr/bin/python3


""" module to write text  to file """


def write_file(filename="", text=""):

    """filename is the file we're writing to
    text is the string to be written"""

    with open(filename, 'w', encoding='utf-8') as f:
        text_written=f.write(text)
