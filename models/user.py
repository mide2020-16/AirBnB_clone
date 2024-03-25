#!/usr/bin/env python3

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
        super().__init__(*args, **kwargs)  # Call the constructor of the superclass (BaseModel)

        # Initialize instance variables with default values or values from kwargs
        self.email = ""  # Email of the user
        self.password = ""  # Password of the user
        self.first_name = ""  # First name of the user
        self.last_name = ""  # Last name of the user
