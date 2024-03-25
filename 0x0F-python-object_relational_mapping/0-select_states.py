#!/usr/bin/python3
"""this is a python script to view all states from a db"""
import MySQLdb
from sys import argv


if __name__ == '__main__':
    db = MySQLdb.connect(host="localhost", user=argv[1],
                         passwd=argv[2], db=argv[3], port=3306)
    cur = db.cursor()
    cur.execute("SELECT * FROM states")
    rows = cur.fetchall()
    for i in rows:
        print(i)
    cur.close()
    db.close()
