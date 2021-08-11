#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from model.city import City
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models import storage

class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nulable=False)
    # make the relationship whith city
    if DBStorage:
        cities = relationship('City', back_populates='state',
                           cascade='all, delete, delete-orphan')
    if FileStorage:
        def cities(self):
            # dictionary of objects of City CLass
            dict_ = storage.all('City')
            # list de ciudades que contiene el state_id == Satae.id
            list_ = []
            for k, v in dict_.items():
                #v es un objeto, porlo tanto debemos acceder
                # a los valores de su dccionario
                if self.id in v.__dict__.values():
                    list_.append(v)
            return list_
