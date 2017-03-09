#!/usr/bin/python3
"""
this script prints all City objects from the database hbtn_0e_6_usa
using SQLAlchemy
"""


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City
if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: username password database name")
    else:
        engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                               (sys.argv[1], sys.argv[2], sys.argv[3]))
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        session = Session()
        cities = session.query(State.name, City.id, City.name).filter(
            State.id == City.state_id).order_by(City.id)
        for city in cities:
            print("{}: ({}) {}".format(city[0], city[1], city[2]))
        session.close()
        engine.dispose()
