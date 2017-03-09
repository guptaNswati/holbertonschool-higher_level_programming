#!/usr/bin/python3
"""
this script lists all states with  N from the database hbtn_0e_0_usa
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
        query = """SELECT * FROM states WHERE name like 'N%'
        ORDER BY id ASC;"""
        cur.execute(query)
        states = cur.fetchall()
        if states:
            for state in states:
                print(state)
        cur.close()
        db.close()
