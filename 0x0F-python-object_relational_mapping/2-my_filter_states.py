import MySQLdb
from sys import argv

# query data from table where data = name passes
if __name__ == '__main__':
    db = MySQLdb.connect(host="localhost", user=argv[1],
                         passwd=argv[2], db=argv[3], port=3306)
    conn = db.cursor()
    conn.execute('SELECT * FROM state WHERE name = "{}"'.format(argv[4]))
    res = conn.fecthall()
    for i in res:
        print(i)
    conn.close()
    db.close()
