#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship, backref
from os import getenv


place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id',
                             String(60),
                             ForeignKey('places.id'),
                             primary_key=True,
                             nullable=False),
                      Column('amenity_id',
                             String(60),
                             ForeignKey('amenities.id'),
                             primary_key=True,
                             nullable=False))


class Place(BaseModel, Base):
    """A place to stay."""
    __tablename__ = 'places'
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        amenity_ids = []

        reviews = relationship('Review', backref='place',
                               cascade="all, delete")
        amenities = relationship('Amenity',
                                 secondary=place_amenity,
                                 viewonly=False)

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
            """Attribute that returns the list of Review """
            list_reviews = []
            all_reviews = models.storage.all(Review)
            for reviews_o in all_reviews:
                if self.id == reviews_o.place_id:
                    list_reviews.append(reviews_o)
            return list_reviews

        @property
        def amenities(self):
            """Attribute that returns the list of Amenity instances"""
            list_amenity = []
            all_amenity = models.storage.all(Amenity)
            for amenity_o in all_amenity.values():
                if amenity_0.id in self.amenity_ids:
                    list_amenity.append(amenity_o)
            return list_amenity

        @amenities.setter
        def amenities(self, obj=None):
            """Attribute that add an Amenity.id to amenity_ids"""
            if obj.__class__.__name__ == 'Amenity':
                self.amenity_ids.append(obj)
