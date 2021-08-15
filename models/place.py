#!/usr/bin/python3
""" Place Module for HBNB project """
from models.amenity import Amenity
from sqlalchemy.sql.elements import Null
from sqlalchemy.sql.sqltypes import Float
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from os import getenv

place_amenity = Table('place_amenity', Base.metadata,
                      Column('places_id', String(60),
                      ForeignKey('places.id'), primary_key=True),
                      Column('amenity_id', String(60),
                      ForeignKey('amenities.id'), primary_key=True)
                      )


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
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)

        user = relationship('User', back_populates='places')
        cities = relationship('City', back_populates='places')
<<<<<<< HEAD
        reviews = relationship(
            'Review', back_populates='place', cascade='all, delete, delete-orphan')
=======
        reviews = relationship('Review', back_populates='place',
                                cascade='all, delete, delete-orphan')
>>>>>>> 82e2ea45061b212d3eecc1f5a3ee5ddd4974ec8a
        amenities = relationship('Amenity', secondary=place_amenity, viewonly=False,
                                 back_populates='place_amenities')

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

        @property
        def reviews(self):
            """

            Returns:
                [type]: [description]
            """
            from models import storage
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

        @property
        def amenities(self):
            """[summary]

            Returns:
                [type]: [description]
            """
            from models import storage
            amenity_objects = list()
            dict_objects = storage.all('Amenity')
            for k, v in dict_objects.items():
                if v.id in self.amenity_ids:
                    amenity_objects.append(v)
            return amenity_objects

        @amenities.setter
        def amenities(self, obj):
            """[summary]

            Args:
                obj ([type]): [description]
            """
            if isinstance(obj, Amenity):
                self.amenity_ids.append(obj)
