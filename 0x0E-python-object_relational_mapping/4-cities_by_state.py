#!/usr/bin/python3
"""
this script  lists all cities from the database
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
        query = """SELECT cities.id, cities.name, states.name FROM cities
        JOIN states On state_id WHERE cities.state_id = states.id
        ORDER BY cities.id ASC;"""
        cur.execute(query)
        cities = cur.fetchall()
        for city in cities:
            print(city)
        cur.close()
        db.close()
