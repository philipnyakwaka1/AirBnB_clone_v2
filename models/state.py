#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='state',
                          cascade='all, delete-orphan')

    @property
    def cities(self):
        from models.engine.file_storage import FileStorage
        qry = FileStorage.all('City')
        cities_list = []
        for val in qry.values():
            if val.state_id == self.id:
                cities_list.append(val)
        return cities_list
