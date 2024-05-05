#!/usr/bin/python3
"""Module for City class."""
from ..models.base_model import BaseModel


class City(BaseModel):
    """City class that inherits from BaseModel."""

    def __init__(self, *args, **kwargs):
        """
        Constructor for City class.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        super().__init__(*args, **kwargs)
        self.state_id = ""
        self.name = ""
