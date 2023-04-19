#!/usr/bin/python3
""" City Module for HBNB project """
from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from os import getenv

class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = "cities"

    if getenv("HBNB_TYPE_STORAGE") == "db":
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    places = relationship("Place", backref="cities", cascade="all, delete, delete-orphan")
    else:
        name = ""
        state_id = ""

        @proprety
        def places(self):
            """ Getter attribute that returns list of Place instances"""
            from models import storage
            places_list = []
            for place in storage.all('Place').values():
                if place.city_id == self.id:
                    places_list.append(place)
            return places_list
