#!/usr/bin/python3
""" Place Module for HBNB project """
from sqlalchemy.sql.sqltypes import Float
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv


class Place(BaseModel, Base):
    """ A place to stay """
    # Revisar la variable de entorno
    storage_type = getenv('HBNB_TYPE_STORAGE')
    # set the atributes of the class (columns name)
    __tablename__ = 'places'
# clase hija de user y de city
    if storage_type == 'db':
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024))
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float)
        longitude = Column(Integer)

        user = relationship('User', back_populates='places')
        cities = relationship('City', back_populates='places')
        reviews = relationship(
            'Review', back_populates='place', cascade='all, delete, delete-orphan')

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

        def reviews(self):
            from models.engine import storage
            # dictionary of objects of City CLass
            dict_ = storage.all('Review')
            # list de ciudades que contiene el state_id == Satae.id
            list_ = []
            for k, v in dict_.items():
                # v es un objeto, porlo tanto debemos acceder
                # a los valores de su dccionario
                if self.id in v.__dict__.values():
                    list_.append(v)
            return list_
