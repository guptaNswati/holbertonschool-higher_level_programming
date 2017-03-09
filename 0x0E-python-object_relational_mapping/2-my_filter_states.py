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
        cur.execute("SELECT * FROM states WHERE name = %s ORDER BY id ASC", (
            sys.argv[4],))
        states = cur.fetchall()
        for state in states:
            print(state)
        cur.close()
        db.close()
