#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from models.state import State
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship



class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = 'cities'
    # set the atributes of the class (columns name)
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    # make relationship with other table
    state = relationship('State', back_populates='cities')

    FileStorage =
