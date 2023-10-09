#!/usr/bin/python3
"""
represnting the BaseModel Class

This module defines the `BaseModel` class,
which serves as the foundation for almost Airbnb objects in the project.
It provides methods for object initialization, serialization,
and deserialization.
"""

from uuid import uuid4
from datetime import datetime
from models import storage


class BaseModel:
    """
    the basse class of all objects in the airbnb project

    Instance Attributes:
        id (str): uniq id for each instance from BaseModel class
        created_at (str): current datetime when an instance is created
        updated_at (str): current datetime when an instance is created and
        it will be updated every time you change your object
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes an instance of the BaseModel class
        """
        if kwargs is not None and len(kwargs.keys()) > 0:
            temp = kwargs.copy()

            self.created_at = datetime.strptime(
                temp["created_at"], "%Y-%m-%dT%H:%M:%S.%f"
            )
            self.updated_at = datetime.strptime(
                temp["updated_at"], "%Y-%m-%dT%H:%M:%S.%f"
            )

            del temp["created_at"]
            del temp["updated_at"]

            if "__class__" in temp.keys():
                del temp["__class__"]

            self.__dict__.update(temp)

            del temp
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(obj=self)

    def save(self):
        """
        Updates the `updated_at` timestamp to the current datetime
        and saves the object to storage.
        This method should be called whenever you make changes to the object.
        """
        updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        Converts the object's attributes to a dictionary for serialization.

        Returns:
            dict: A dictionary containing the object's attributes.
                '__class__': The name of the object's class.
                'created_at': ISO-formatted string of the 'created_at' attr.
                'updated_at': ISO-formatted string of the 'updated_at' attr.
                Other attributes specificied when object Initialized.
        """
        returned_dict = self.__dict__.copy()
        returned_dict["__class__"] = self.__class__.__name__
        returned_dict["created_at"] = self.created_at.isoformat()
        returned_dict["updated_at"] = self.updated_at.isoformat()
        return returned_dict

    def __str__(self):
        """
        Returns a string representation of the object
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
