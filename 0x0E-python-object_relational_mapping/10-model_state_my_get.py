#!/usr/bin/python3
"""
this script prints the State object with the given name from hbtn_0e_6_usa
using SQLAlchemy
"""


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: username password database name state")
    else:
        engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                               (sys.argv[1], sys.argv[2], sys.argv[3]))
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        session = Session()
        states = session.query(State.id).filter(
            State.name == sys.argv[4]).order_by(State.id).all()
        if states:
            for state in states:
                print("{}".format(state[0]))
        else:
            print("Not found")
        session.close()
        engine.dispose()
