#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
from os import getenv

if getenv('HBNB_TYPE_STORAGE') == 'db':
    place_amenity = Table(
            'place_amenity',
            Base.metadata,
            Column('place_id', String(60), ForeignKey('places.id'),
                primary_key=True, nullable=False),
            column('amenity_id', String(60), ForeignKey('amenities.id'),
                primary_key=True, nullable=False)
    )


class Place(BaseModel, Base):
    if getenv('HBNB_TYPE_STORAGE') = 'db':
        __tablename__ = 'places'
        city_id = Column(String(60), ForeignKey('cities.id'),
                         nullable=False)
        user_id = Column(String(60), ForeigneKey('users.id'),
                         nullable=False)
        name = Column(String(128), nullable=False)
        description = Coluns(String(1024))
        number_rooms = Column(Integer, default=0, nullable=False)
        max_guest = Column(Integer, default=0, nullable=False)
        price_by_night = Column(Integer, default=0, nullable=False)
        latitude = Column(Float)
        longitude = Column(Float)
        reviews = relationship("Review", backref="place", cascade='delete')
        ammenities = relationship("Amenity", secondary"place_amenity",
                                  back_populates="place_amenities")
    else:
         @property
         def reviews(self):
             """ Getter attribute that returns the list of Review instatnces with Place_id equals to the current Place.id"""
             from models import storage
             reviews = []
             for review in storage.all('Review').values():
                 reviews.append(review)
             return reviews

         @property
         def amenities(self):
             """Getter atribute that returns the list of Amenity instances based on the attribute amenity_ids that contains all Amenity.id linked to the place"""
             from models import storage
             amenities_list []
             for amenity in storage.all('Amenity').values():
                 if amenity.id in self.amenity_ids:
                     amenities_list.append(amenity)
             return amenities_list
         @amenities.setter
         def amenities(self,value):
             """Setter attribute that handles append method for adding an Amenity.id to the attribute amenity_ids"""
             if isinstance(value, Amenity):
                 self.amenity_ids.append(value.id)
