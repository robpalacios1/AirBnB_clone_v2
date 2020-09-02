#!/usr/bin/python3
"""Engine DBStorage Module"""
from models.base_model import BaseModel, Base
from models.city import City
from models.state import State
from models.user import User
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine
from os import getenv


class DBStorage:
    """New Engine
    Attributes:
        engine: set to None
        session: set to None
    """
    __engine = None
    __session = None

    def __init__(self):
        """This class manage Storage for Database"""
        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}:3306/{}'
            .format(getenv("HBNB_MYSQL_USER"),
                    getenv("HBNB_MYSQL_PWD"),
                    getenv("HBNB_MYSQL_HOST"),
                    getenv("HBNB_MYSQL_DB")),
            pool_pre_ping=True)

        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """all objects depending of the class name"""
        clss = [State,
                City,
                User,
                Place,
                Review,
                Amenity]
        objs = []
        _dic = {}

        if cls:
            objs = self.__session.query(cls).all()
        else:
            for cls in clss:
                objs += self.__session.query(cls)

        for obj in objs:
            key = "{}.{}".format(type(obj).__name__, str(obj.id))
            _dic[key] = obj

        return _dic

    def new(self, obj):
        """add the object to the current database session"""
        if obj:
            self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """create all tables in the database"""

        Base.metadata.create_all(self.__engine)

        Session = scoped_session(sessionmaker(bind=self.__engine,
                                              expire_on_commit=False))

        self.__session = Session()

    def close(self):
        """call method on the private session"""
        self.__session.close()
