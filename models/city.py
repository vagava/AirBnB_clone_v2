#!/usr/bin/python3
""" City Module for HBNB project """
from models.state import State
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv

# child


class City(BaseModel, Base):
    """ The city class, contains state ID and name """

    # Revisar la variable de entorno
    storage_type = getenv('HBNB_TYPE_STORAGE')
    # set the atributes of the class (columns name)
    __tablename__ = 'cities'
# clase padre de places y la clase hija de state
    if storage_type == 'db':
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        # State ->  nombre de la clase padre
        # cities -> nombre de la tabla de a clase hija (City)
        state = relationship('State', back_populates='cities')

        places = relationship('Place', back_populates='cities',
                              cascade='all, delete, delete-orphan')
    else:
        name = ''
        state_id = ''
