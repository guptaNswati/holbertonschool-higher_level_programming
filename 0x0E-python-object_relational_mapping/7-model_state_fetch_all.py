#!/usr/bin/python3
# this script lists all states from the database hbtn_0e_6_usa using SQLAlchemy
import sys
from sqlalchemy import create_engine
engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]))
conn = engine.connect()
states = conn.execute("SELECT * FROM states")
for state in states:
    print("{:d}: {:s}".format(state[0], state[1]))
