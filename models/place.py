#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy import *
from sqlalchemy.orm import relationship
from os import getenv

place_amenity = Table("place_amenity",
                      Base. metadata,
                      Column("place_id", String(60),
                             ForeignKey("places.id"),
                             primary_key=True,
                             nullable=False),
                      Column("amenity_id", String(60),
                             ForeignKey("amenities.id"),
                             primary_key=True,
                             nullable=False))


class Place(BaseModel, Base):
    """A place to stay """

    __tablename__ = "places"

    city_id = Column(String(60),
                     ForeignKey("cities.id", ondelete="CASCADE"),
                     nullable=False)
    user_id = Column(String(60),
                     ForeignKey("users.id", ondelete="CASCADE"),
                     nullable=False)
    name = Column(String(128),
                  nullable=False)
    description = Column(String(1024),
                         nullable=True)
    number_rooms = Column(Integer,
                          nullable=False,
                          default='0')
    number_bathrooms = Column(Integer,
                              nullable=False,
                              default='0')
    max_guest = Column(Integer,
                       nullable=False,
                       default='0')
    price_by_night = Column(Integer,
                            nullable=False,
                            default='0')
    latitude = Column(Float,
                      nullable=True)
    longitude = Column(Float,
                       nullable=True)

    amenity_ids = []

    if getenv("HBNB_TYPE_STORAGE") == "db":
        reviews = relationship("Review", backref="place",
                               cascade="all, delete")

        amenities = relationship("Amenity",
                                 secondary='place_amenity',
                                 viewonly=False,
                                 back_populates="place_amenities")

    else:
        @property
        def amenities(self):
            """Returns the list of Amenity"""
            _list = []
            for obj in amenity_ids:
                if obj.id == self.id:
                    _list.append(obj)
            return (_list)

        @amenities.setter
        def amenities(self, obj):
            """Handles append method for adding an Amenity.id"""
            if type(obj).__name__ == 'Amenity':
                self.amenity_ids.append(obj)
