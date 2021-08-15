#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv


class Amenity(BaseModel, Base):

    storage_type = getenv('HBNB_TYPE_STORAGE')
    # set the atributes of the class (columns name)
    __tablename__ = 'amenities'

    if storage_type == 'db':
        name = Column(String(128), nullable=False)
    else:
        name = ""

    place_amenities = relationship('Place', secondary=place_amenity,
                                   back_populates='amenities')
