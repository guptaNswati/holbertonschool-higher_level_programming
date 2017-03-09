#!/usr/bin/python3
"""
this script  lists all cities from the database
"""
import sys
import MySQLdb
db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
cur = db.cursor()
cur.execute("SELECT cities.id, cities.name, states.name FROM cities JOIN states On state_id WHERE cities.state_id = states.id")
cities = cur.fetchall()
for city in cities:
    print(city)
db.close()
