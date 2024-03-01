#!/usr/bin/python3
import sys
import urllib.request
with urllib.request.urlopen(sys.argv[1]) as response:
    id = response.info().get("X-Request-Id")
    print(id)
