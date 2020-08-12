#!/usr/bin/python3
"""This is the state class"""
from models.base_model import BaseModel, Base
import models
from models.city import City
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
import os


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    if os.getenv("HBNB_TYPE_STORAGE") == "db":
        cities = relationship("City", cascade="all, delete-orphan",
                              backref="state")

    else:
        """File Storage"""
        @property
        def cities(self):
            """
            city properties
            """
            city = []
            for val in models.storage.all(City).values():
                if val.state_id == self.id:
                    city.append(val)
            return city