#!/usr/bin/python3
"""
representing the User class

This module defines the `User` class, which inherits from the `BaseModel` class.
The `User` class represents user objects and includes attributes for email, password, first name, and last name.
It provides methods for object initialization and can be used to create, update, and manage user objects.
"""

from models.base_model import BaseModel


class User(BaseModel):
    """
    The `User` class represents user objects and includes attributes for email, password, first name, and last name.
    It provides methods for object initialization and can be used to create, update, and manage user objects.

    Class Attributes:
        email (str): The email address of the user.
        password (str): The user's password.
        first_name (str): The first name of the user.
        last_name (str): The last name of the user.
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """
        initialization method for User class

        kwargs: key, value pairs each key will be an attribute
        """
        super().__init__(*args, **kwargs)
