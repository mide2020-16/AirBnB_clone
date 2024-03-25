#!/usr/bin/python3
"""Module for Review class."""
from models.base_model import BaseModel


class Review(BaseModel):
    """Review class that inherits from BaseModel."""

    def __init__(self, *args, **kwargs):
        """
        Constructor for Review class.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        super().__init__(*args, **kwargs)  # Call the constructor of the superclass (BaseModel)

        # Initialize instance variables with default values or values from kwargs
        self.place_id = ""  # ID of the place being reviewed
        self.user_id = ""  # ID of the user who wrote the review
        self.text = ""  # Text content of the review
