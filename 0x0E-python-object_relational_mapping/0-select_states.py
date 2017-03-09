#!/usr/bin/python3
"""
this script lists all states from the database hbtn_0e_0_usa
"""


import sys
import MySQLdb
if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: username password, databasename")
    else:
        db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                             db=sys.argv[3])
        cur = db.cursor()
        cur.execute("SELECT * FROM states ORDER BY id ASC")
        states = cur.fetchall()
        for state in states:
            print(state)
        cur.close()
        db.close()
