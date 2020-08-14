#!/usr/bin/python3
"""DB Storage."""

from os import getenv
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy import create_engine
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models.base_model import BaseModel, Base


class DBStorage:
    """DB storage class."""
    __engine = None
    __session = None

    def __init__(self):
        """Method init for DBStorage."""
        username = getenv('HBNB_MYSQL_USER')
        password = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        db_base = getenv('HBNB_MYSQL_DB')

        # Create a new Engine instance.
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}:3306/{}'
                                      .format(username,
                                              password,
                                              host,
                                              db_base),
                                      pool_pre_ping=True)  # test connections.
        # Drop all tables if the env == test
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """Get all objects."""
        new_dict = {}  # Dictionary with all objects
        if cls is None:
            classes = ['Amenity', 'City', 'Place', 'Review', 'State', 'User']
            for my_class in classes:
                # Contain all objects of my_class
                my_query = self.__session.query(eval(my_class))
                for obj_query in my_query:
                    key = type(obj_query).__name__ + "." + str(obj_query.id)
                    new_dict[key] = obj_query
        else:
            # Contain all objects of cls.
            my_query = self.__session.query(cls)
            for obj_query in my_query:
                key = type(obj_query).__name__ + "." + str(obj_query.id)
                new_dict[key] = obj_query
        return new_dict

    def new(self, obj):
        """Add the object to the current database session """
        self.__session.add(obj)

    def save(self):
        """ Commit all changes of the current database session """
        self.__session.commit()

    def delete(self, obj=None):
        """ Delete from the current database session """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """ Create all tables stored in this metadata """
        Base.metadata.create_all(bind=self.__engine)
        Session = scoped_session(sessionmaker(bind=self.__engine,
                                              expire_on_commit=False))
        self.__session = Session()
