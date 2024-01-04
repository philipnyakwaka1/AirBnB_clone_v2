#!/usr/bin/python3
"""This module defines a class to manage db storage for hbnb clone"""

from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv
from models.base_model import Base
from models.city import City
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.user import User
from models.review import Review
from models.state import State


class DBStorage:
    """This class manages db storage of hbnb models"""

    __engine = None
    __session = None

    def __init__(self):
        """Creates an engine"""

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(getenv('HBNB_MYSQL_USER'),
                                              getenv('HBNB_MYSQL_PWD'),
                                              getenv('HBNB_MYSQL_HOST'),
                                              getenv('HBNB_MYSQL_DB')),
                                      pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
            from models.base_model import BaseModel, Base
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """queries the database"""
        storage_dictionary = {}
        classes = [User, State, City, Amenity, Place, Review]
        if not cls:
            for cl in classes:
                try:
                    for record in self.__session.query(cl).all():
                        if record:
                            storage_dictionary[record.__class__.__name__ +
                                               '.' + record.id] = record
                except Exception as e:
                    pass
        elif cls and cls in classes:
            qry = self.__session.query(cls).all()
            for obj in qry:
                storage_dictionary[obj.__class__.__name__ + '.' + obj.id] = obj
        return storage_dictionary

    def new(self, obj):
        """
        add the object to the current database session (self.__session)
        """
        self.__session.add(obj)

    def save(self):
        """
        commit all changes of the current database session (self.__session)
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        delete from the current database session obj if not None
        """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """
        reloads
        """
        Base.metadata.create_all(self.__engine)
        new_session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(new_session)
        self.__session = Session()

    def close(self):
        """***closes***"""

        self.__session.remove()
