#!/usr/bin/python3
"""
This module defines the `Review` class,
which represents reviews for places in the Airbnb project.
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """
    The `Review` class represents reviews for places in the Airbnb project.

    Class Attributes:
        place_id (str): The identifier of the place being reviewed.
        user_id (str): The identifier of the user who wrote the review.
        text (str): The text content of the review.
    """

    place_id = ""
    user_id = ""
    text = ""
