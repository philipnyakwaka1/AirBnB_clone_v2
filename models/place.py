#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import ForeignKey, Column, String, Integer, Float
from sqlalchemy.orm import relationship
import os


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        reviews = relationship('Review', backref='places',
                               cascade='all, delete-orphan')
    else:
        @property
        def reviews(self):
            """
            getter attribute reviews that returns the list of Review
            instances with place_id equals to the current Place.id =>
            It will be the FileStorage relationship between Place and Review
            """
            from models.engine.file_storage import FileStorage
            qry = FileStorage.all('Reviews')
            cities_list = []
            for val in qry.values():
                if val.place_id == self.id:
                    cities_list.append(val)
            return cities_list
