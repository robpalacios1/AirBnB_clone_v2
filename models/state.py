#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship, backref
from os import getenv
import models


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship('City', backref='state',
                              cascade="all, delete")
    else:
        name = ""

        @property
        def cities(self):
            """Attribute that returns the list of City."""
            list_cities = []
            all_cities = models.storage.all(City)
            for city_o in all_cities:
                if self.id == city_o.state_id:
                    list_cities.append(city_o)
            return list_cities
