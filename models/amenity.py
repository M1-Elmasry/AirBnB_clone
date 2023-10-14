#!/usr/bin/python3
"""
This module defines the `Amenity` class,
which represents amenities available in accommodations.
"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    The `Amenity` class represents amenities available in accommodations.

    Class Attributes:
        name (str): The name of the amenity.
    """

    name = ""
