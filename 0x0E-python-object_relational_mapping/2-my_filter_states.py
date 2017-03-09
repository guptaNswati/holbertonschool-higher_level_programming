#!/usr/bin/python3
"""
this script displays all values in the states table of hbtn_0e_0_usa
where name matches the argument.
"""


import sys
import MySQLdb
if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: username password, databasename state")
    else:
        db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                             db=sys.argv[3])
        cur = db.cursor()
        query = "SELECT * FROM states WHERE BINARY name = '{:s}' \
        ORDER BY id ASC".format(sys.argv[4])
        cur.execute(query)
        states = cur.fetchall()
        if states:
            for state in states:
                print(state)
        cur.close()
        db.close()
