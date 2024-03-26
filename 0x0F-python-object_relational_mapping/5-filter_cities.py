#!/usr/bin/python3
"""query data from table where data = name passes, sql injection free"""
import MySQLdb
from sys import argv

if __name__ == '__main__':
    db = MySQLdb.connect(host="localhost", user=argv[1],
                         passwd=argv[2], db=argv[3], port=3306)
    conn = db.cursor()
    conn.execute('SELECT * FROM cities WHERE name = ?', argv[4])
    res = conn.fetchall()
    for i in res:
        print(i)
    conn.close()
    db.close()
