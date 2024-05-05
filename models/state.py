#!/usr/bin/python3
"""Module for State class."""
from ..models.base_model import BaseModel


class State(BaseModel):
    """State class that inherits from BaseModel."""

    def __init__(self, *args, **kwargs):
        """
        Constructor for State class.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        super().__init__(*args, **kwargs)
        self.name = ""
