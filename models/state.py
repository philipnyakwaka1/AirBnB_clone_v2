#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base, storage
from models.city import City
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
import os


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='state',
                          cascade='all, delete-orphan')

    if os.getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def cities_list(self):
            cities_list = []
            for val in list(storage.all().values()):
                if val.state_id == self.id:
                    cities_list.append(val)
            return cities_list
