#!/usr/bin/python3
"""
This module defines the `City` class,
which represents cities in the Airbnb project.
"""

from models.base_model import BaseModel


class City(BaseModel):
    """
    The `City` class represents cities in the Airbnb project.

    Class Attributes:
        state_id (str): The identifier of the state associated with the city.
        name (str): The name of the city.
    """

    state_id = ""
    name = ""
