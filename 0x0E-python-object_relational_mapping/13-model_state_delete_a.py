#!/usr/bin/python3
"""
this script deletes all State objects with a name containing the letter 'a'
from the database hbtn_0e_6_usa using SQLAlchemy
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
        to_del = session.query(State).filter(State.name.ilike('%a%')).all()
        if to_del:
            for i in to_del:
                session.delete(i)
        session.commit()
        session.close()
        engine.dispose()
