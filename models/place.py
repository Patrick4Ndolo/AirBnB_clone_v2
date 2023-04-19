#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
from os import getenv

if getenv('HBNB_TYPE_STORAGE') = 'db':
    place_amenity = Table(
            'place_amenity',
            Base.metadata,
            Column('place_id', String(60), Foreignkey('places.id'),
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
                                  bacl_populates="place_amenities")
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

    def __init__(self, *args, **kwargs):
        super().__init(*args, **kwargs)

        if getenv('HBNB_TYPE_STORAGE') !='db':
            self.amenities = []

