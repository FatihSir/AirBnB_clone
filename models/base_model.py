#!/usr/bin/python3
"""Base Model Module"""


from uuid import uuid4
from datetime import datetime


class BaseModel:
    """
    BaseModel class defines all common attributes/methods for other classes
    """
    def __init__(self):
        """
        Initialization method defines the basic information
        when an instance is created

        Arguments:
        id (str): A unique ID that will be given to each instance
        created_at (datetime object) : the creation time of an instance
        updated_at (datetime object) : the updating time of an instance
        """
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        """ A method the returns information about an object

        Return:a string representation of the object
        """
        return f"[{self.__class__.__name__}] ({self.id}) ({self.__dict__})"

    def save(self):
        """ A method that updates the public instance attribute
        updated_at with the current datetime """
        self.updated_at = datetime.now()

    def to_dict(self):
        """A method  returns a dictionary containing all
           keys/values of __dict__ of the instance

        Return: a dictionary that contains object's information

        """
        self.__dict__['__class__'] = self.__class__.__name__
        self.__dict__['created_at'] = datetime.isoformat(self.created_at)
        self.__dict__['updated_at'] = datetime.isoformat(self.updated_at)

        return self.__dict__
