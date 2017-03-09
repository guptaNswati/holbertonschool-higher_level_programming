#!/usr/bin/python3
"""
this script lists all states containing 'a' from hbtn_0e_6_usa
using SQLAlchemy
"""


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: username password database name")
    else:
        engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                               (sys.argv[1], sys.argv[2], sys.argv[3]))
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        session = Session()
        for state in session.query(State.id, State.name).filter(
                State.name.ilike('%a%')).order_by(State.id):
            print("{:d}: {:s}".format(state[0], state[1]))
        session.close()
        engine.dispose()
