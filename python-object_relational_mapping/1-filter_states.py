#!/usr/bin/python3
"""module"""
import MySQLdb
import sys


if __name__ == '__main__':

    db = MySQLdb.connect(host="localhost",
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3],
                         port=3306)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE binary 'N%'"
                "ORDER BY states.id ASC")
    for states in cur.fetchall():
        print(states)
    cur.close()
    db.close()
