#!/usr/bin/python3
""" Place Module for HBNB project """
from sqlalchemy.sql.sqltypes import Float
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv


class Place(BaseModel):
    """ A place to stay """
    # Revisar la variable de entorno
    storage_type = getenv('HBNB_TYPE_STORAGE')
    # set the atributes of the class (columns name)
    __tablename__ = 'places'

    if storage_type == 'db':
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024))
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=False, default=0)
        longitude = Column(Integer, nullable=False, default=0)

        cities = relationship('City', back_populates='places')

        user = relationship('User', back_populates='users')

    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []
