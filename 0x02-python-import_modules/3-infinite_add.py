#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argc = len(sys.argv) - 1
    total = 0
    if argc == 0:
        print("0")
    else:
        for i in range(1, len(sys.argv)):
            total += int(sys.argv[i])
        print("{}".format(total))
