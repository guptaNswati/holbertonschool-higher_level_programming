#!/usr/bin/python3
"""
This module contains class definition of a City and an instance of
declarative_base() called Base
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class City(Base):
    """
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False, unique=True,
                autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)

    def __str__(self):
        """
        """
        return "{}: ({}) {}".format(self.id, self.state_id, self.name)

    def __repr__(self):
        """
        """
        return "City(name={}, id={}, state_id={})".format(self.name,
                                                          self.id,
                                                          self.state_id)
