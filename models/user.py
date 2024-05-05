#!/usr/bin/python3

from models.base_model import BaseModel

class User(BaseModel):
    """User class that inherits from BaseModel."""

    def __init__(self, *args, **kwargs):
        """
        Constructor for User class.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        super().__init__(*args, **kwargs)

        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""
