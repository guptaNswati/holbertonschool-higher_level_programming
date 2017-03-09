#!/usr/bin/python3
"""
this script displays all values in the states table of hbtn_0e_0_usa
where name matches the argument, safe from MySQL injection!
"""


import sys
import MySQLdb
if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: username, password, database name and state")
    else:
        db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                             db=sys.argv[3])
        cur = db.cursor()
        cur.execute("SELECT * FROM states WHERE name = %s", (sys.argv[4],))
        states = cur.fetchall()
        for state in states:
            print(state)
        cur.close()
        db.close()
