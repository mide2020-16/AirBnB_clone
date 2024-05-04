#!/usr/bin/env python3

"""
The Base Model - It defines all attributes and methods
"""
from uuid import uuid4
from datetime import datetime
from models import storage

class BaseModel:
    """
        The Base Model is used to manipulate instances and serialization and deserialization
    """

    id = str(uuid4())
    created_at = datetime.now()
    updated_at = datetime.now()

    def __init__(self, *args, **kwargs):
        """
        Initialises the BaseModel instances
        """

        if kwargs and not args:
            for key, value in kwargs.items():
                if key == "updated_at" or key == "created_at":
                    setattr(self, key, datetime.fromisoformat(value))
                elif key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            storage.new(self)

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {vars(self)}"

    def save(self):
        """
        Saves and updates instances 'updated_at'
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        Returns A dictionary containing all keys/values of __dict__ of the instances
        """
        d = vars(self).copy()
        d["__class__"] = self.__class__.__name__
        d["created_at"] = datetime.isoformat(self.created_at)
        d["updated_at"] = datetime.isoformat(self.updated_at)
        return d
