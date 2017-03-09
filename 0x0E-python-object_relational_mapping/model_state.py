#!/usr/bin/python3
"""
This module contains class definition of a State and an instance Base
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    """
    Initiates State object
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, unique=True,
                autoincrement=True)
    name = Column(String(128), nullable=False)

    """
    Print object
    """
    def __str__(self):
        return "{}: {}".format(self.name, self.id)

    """
    String representation of the object
    """
    def __repr__(self):
        return "State(name={}, id={})".format(self.name, self.id)
