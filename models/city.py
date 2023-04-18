#!/usr/bin/python3
""" City Module for HBNB project """
from od import getenv
from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel


class City(BaseModel):
    """ The city class, contains state ID and name """
    __tablename__ = "cities"
    name = Column(String(128), nullable=False)
    state_id = String(60), ForeignKey('states.id'), nullable=False)
    places = relationship("Place", backref="cities", cascade='all, delete, delete-orphan")

