#!/usr/bin/python3
"""File Storage Module"""


from models.base_model import BaseModel
import json
import os


class FileStorage:
    """
    A class that serializes instances to a JSON file and
    deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """A method that returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """ A method that sets in __objects the obj with
            key <obj class name>.id """
        class_name = obj.__class__.__name__
        key = class_name + "." + str(obj.id)
        self.__objects[key] = obj

    def save(self):
        """ A method that serializes __objects to the
            JSON file (path: __file_path) """
        with open(file=self.__file_path, mode='w') as f:
            json.dump(
                {key: value.to_dict() for key,
                 value in self.__objects.items()}, f)

    def reload(self):
        """
        deserializes the JSON file to __objects only if the JSON file exists
        otherwise, do nothing. If the file does not exist,
        no exception should be raised
        """

        if not os.path.exists(self.__file_path):
            return

        with open(file=self.__file_path, mode='r') as f:
            des = None
            try:
                des = json.load(f)
            except json.JSONDecodeError:
                pass

            if des is None:
                return

            self.__objects = {
                k: BaseModel(**v)
                for k, v in des.items()}
