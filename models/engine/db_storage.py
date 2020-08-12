#!/usr/bin/python3
"""
'db_storage' module
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
import os
from models.base_model import BaseModel, Base
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.user import User
from models.review import Review

database = os.getenv("HBNB_MYSQL_DB")
host = os.getenv("HBNB_MYSQL_HOST")
password = os.getenv("HBNB_MYSQL_PWD")
user = os.getenv("HBNB_MYSQL_USER")

instances = {"State": State, "City": City, "Amenity": Amenity,
             "User": User, "Review": Review, "Place": Place}


class DBStorage():
    """
    DBStorage class
    """
    __engine = None
    __session = None

    def __init__(self):
        """
        creates engine
        """
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}"
                                      .format(user, password, host, database),
                                      pool_pre_ping=True)
        if os.getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """
        prints all objects in database
        """
        instlist = [State, City, User]
        new_dict = {}
        if cls:
            for obj in self.__session.query(instances[cls]).all():
                key = str(obj.__class__.__name__) + "." + str(obj.id)
                value = obj
                new_dict[key] = value
            return new_dict
        else:
            for inst in instlist:
                for obj in self.__session.query(inst).all():
                    key = str(inst.__name__) + "." + str(obj.id)
                    value = obj
                    new_dict[key] = value
            return new_dict

    def new(self, obj):
        """
        adds the object to the current database session
        """
        self.__session.add(obj)

    def save(self):
        """
        commit all changes of the current database session
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        delete from current database session 'obj' if not None
        """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """
        create all tables in the database
        """
        Base.metadata.create_all(bind=self.__engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Scoped = scoped_session(Session)
        self.__session = Scoped

    def close(self):
        """
        remove method on private session attribute
        """
        self.__session.remove()