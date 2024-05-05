#!/usr/bin/python3
"""Module for Amenity class."""
from ..models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity class that inherits from BaseModel."""

    def __init__(self, *args, **kwargs):
        """
        Constructor for Amenity class.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        super().__init__(*args, **kwargs)
        self.name = ""
