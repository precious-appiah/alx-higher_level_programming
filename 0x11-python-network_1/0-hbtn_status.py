#!/usr/bin/python3
import urllib.request
with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    res = response.read()
    print(f"Body response:\n\t- type: {type(res)}\n\t- content: {res}\n\t- utf-8 content: {res.decode('utf-8')}")
