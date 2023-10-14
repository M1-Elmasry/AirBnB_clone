#!/usr/bin/python3
"""
This module defines the `State` class,
which represents states in the Airbnb project.
"""

from models.base_model import BaseModel


class State(BaseModel):
    """
    The `State` class represents states in the Airbnb project.

    Class Attributes:
        name (str): The name of the state.
    """

    name = ""
