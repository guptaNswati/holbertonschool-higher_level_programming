#!/usr/bin/python3
"""
this script lists all cities of given state
"""
import sys
import MySQLdb
if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: username password database name state")
    else:
        db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                             db=sys.argv[3])
        cur = db.cursor()
        query = """SELECT cities.name FROM cities WHERE state_id IN
        (SELECT states.id FROM states WHERE name = %s);"""
        cur.execute(query, (sys.argv[4],))
        cities = cur.fetchall()
        for i in range(len(cities) - 1):
            print(cities[i][0], end=", ")
        print(cities[i + 1][0])
        cur.close()
        db.close()