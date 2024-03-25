#!/usr/bin/python3
"""queries data starting with 'N' """

import MySQLdb
from sys import argv

if __name__ == '__main__':
    db = MySQLdb.connect(host="localhost", user=argv[1],
                         passwd=argv[2], db=argv[3], port=3306)
    conn = db.cursor()
    conn.execute('SELECT * FROM states  WHERE name LIKE "N%";')
    res = conn.fetchall()
    for i in res:
        print(i)
    conn.close()
    db.close()
