#!/usr/bin/python3
"""
    Once again, write a script that takes in arguments and displays all values
    in the states table of hbtn_0e_0_usa where name matches the argument.
    But this time, write one that is safe from MySQL injections!

    Your script should take 4 arguments: mysql username, mysql password,
    database name and state name searched (safe from MySQL injection)
    You must use the module MySQLdb (import MySQLdb)
    Your script should connect to a MySQL server running on localhost at port
    3306
    Results must be sorted in ascending order by states.id
    Results must be displayed as they are in the example below
    Your code should not be executed when imported
"""
import MySQLdb
import sys


if __name__ == '__main__':

    db = MySQLdb.connect(host="localhost",
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3],
                         port=3306)
    cur = db.cursor()
    cur.execute("""SELECT cities.id, cities.name, states.name FROM cities
                LEFT JOIN
                states ON cities.state_id = states.id WHERE states.name=%s
                ORDER by cities.id ASC""",
                (sys.argv[4], ))
    line = cur.fetchall()
    for i, city in enumerate(line, start=0):
        # each word (!= 0), add a comma
        if i != 0:
            print(", ", end="")
        print(city[1], end="")
    print()
    cur.close()
    db.close()
