#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import COlumn, String
from sqlalchemy.orm import relationship
from os import getenv


class Amenity(BaseModel, Base):
    """A class that creates different amenities"""
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = 'amenities'
        name = Column(String(128), nullable=False)
        place_amenities = relatioship("Place", secondary="place_amenity", back_populates="amenities")
    else:
        name = ""
