#!/usr/bin/python3
import sys
import urllib.request
with urllib.request.urlopen(sys.argv[1]) as response:
    res_arr = response.headers.items()
    for (x, y) in res_arr:
        if x == "X-Request-Id":
            print(y)
