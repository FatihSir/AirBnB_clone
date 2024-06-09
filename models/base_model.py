#!/usr/bin/python3
"""Base Model Module"""


from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """
    BaseModel class defines all common attributes/methods for other classes
    """
    def __init__(self, *args, **kwargs):
        """
        Initialization method defines the basic information
        when an instance is created

        Arguments:
        *args (tuple): Will not be used
        **kwargs (dict): the attributes of the instance in dict format
        """
        if len(kwargs) >= 1:
            for attr, value in kwargs.items():
                if attr == "__class__":
                    continue
                if attr == "updated_at" or attr == "created_at":
                    setattr(self, attr, datetime.fromisoformat(value))
                setattr(self, attr, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at

            models.storage.new(self)

    def __str__(self):
        """ A method the returns information about an object

        Return:a string representation of the object
        """
        return f"[{self.__class__.__name__}] ({self.id}) ({self.__dict__})"

    def save(self):
        """
        A method that updates the public instance attribute
        updated_at with the current datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """A method  returns a dictionary containing all
        keys/values of __dict__ of the instance

        Return:
            self.__dict__ (dict): a dictionary that contains object's
            information
        """

        my_dict = dict(**self.__dict__)
        my_dict['__class__'] = self.__class__.__name__
        my_dict['created_at'] = my_dict['created_at'].isoformat()
        my_dict['updated_at'] = my_dict['updated_at'].isoformat()

        return my_dict
