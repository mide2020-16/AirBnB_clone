#!/usr/bin/python3

from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

class User(BaseModel):
    """User class that inherits from BaseModel."""


    storage = FileStorage()
    storage.reload()
    
    def __init__(self, *args, **kwargs):
        """
        Constructor for User class.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        super().__init__(*args, **kwargs)  # Call the constructor of the superclass (BaseModel)

        # Initialize instance variables with default values or values from kwargs
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""

