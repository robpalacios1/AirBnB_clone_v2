#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns the list of objects of one type of class.
        Args:
            cls: Class
        Return:
            returns the list of objects of one type of class.
        """
        _dic = {}
        if cls is None:
            return (self.__objects)
        else:
            for key, value in self.__objects.items():
                if isinstance(value, cls):
                    _dic[key] = value
            return _dic

    def new(self, obj):
        """Adds new object to storage dictionary"""
        if obj:
            self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Saves storage dictionary to file"""
        temp = {}
        for key, val in self.__objects.items():
            temp[key] = val.to_dict()
        with open(self.__file_path, 'w', encoding='utf-8') as f:
            json.dump(temp, f, indent=4)

    def delete(self, obj=None):
        """delete obj from __objects if it’s inside
        Args:
            obj: Object
        """
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            if key in self.__objects:
                del self.__objects[key]
            self.save()

    def reload(self):
        """Loads storage dictionary from file"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
            'BaseModel': BaseModel, 'User': User, 'Place': Place,
            'State': State, 'City': City, 'Amenity': Amenity,
            'Review': Review
        }
        try:
            temp = {}
            with open(self.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass

    def close(self):
        """call method for deserializing"""
        self.reload()
