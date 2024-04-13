#!/usr/bin/python3
"""The Base Model Module"""


from uuid import uuid4
from datetime import datetime


class BaseModel:
    """The BaseModel class"""

    def __init__(self):
        """
        Initialization method to set a unique id
        and save creation time
        """

        self.id = str(uuid4())
        self.created_at = str(datetime.now().isoformat())
        self.updated_at = self.created_at

    def __str__(self):
        """A method returns information about the instance"""
        return "[{}] ({}) {}".format
        (self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """A method to update updated_at to the current time"""
        self.updated_at = str(datetime.now().isoformat())

    def to_dict(self):
        """
        A method that returns a dictionary containing
        all keys/values of __dict__ of the instance

        Return:
            info (dict): dictionary contains instance's information
        """
        info = {"__class__": self.__class__.__name__}
        for key, value in self.__dict__.items():
            info[key] = value
