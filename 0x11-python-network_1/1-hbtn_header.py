#!/usr/bin/python3
from sys import argv
import urllib.request
with urllib.request.urlopen(argv[1]) as response:
    res_arr = response.headers.items()
    for (x, y) in res_arr:
        if x == "X-Request-Id":
            print(y)
