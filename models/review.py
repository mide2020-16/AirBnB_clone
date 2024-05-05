#!/usr/bin/python3
"""Module for Review class."""
from ..models.base_model import BaseModel


class Review(BaseModel):
    """Review class that inherits from BaseModel."""

    def __init__(self, *args, **kwargs):
        """
        Constructor for Review class.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        super().__init__(*args, **kwargs)
        self.place_id = ""
        self.user_id = ""
        self.text = ""
