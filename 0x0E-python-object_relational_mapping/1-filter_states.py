#!/usr/bin/python3
# this script lists all states with  N from the database hbtn_0e_0_usa
import sys
import MySQLdb
db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
cur = db.cursor()
cur.execute("SELECT * FROM states WHERE name like 'N%'")
states = cur.fetchall()
for state in states:
    print(state)
