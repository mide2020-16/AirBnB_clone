#!/usr/bin/env python3
import json
from models.user import User
from base_model import BaseModel

class FileStorage:
    """FileStorage class for managing serialization and deserialization of objects to/from JSON file."""

    __file_path = 'file.json'  # Path to the JSON file
    __objects = {}  # Dictionary to store serialized objects

    classes = {  # Dictionary mapping class names to their corresponding classes
        "BaseModel": BaseModel,
        "User": User
    }

    def all(self):
        """Retrieve all stored objects."""
        return self.__objects

    def new(self, obj):
        """Add a new object to the storage dictionary."""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serialize objects and save them to the JSON file."""
        serialized_objs = {}

        for key, obj in self.__objects.items():
            serialized_objs[key] = obj.to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(serialized_objs, f)

    def reload(self):
        """Deserialize objects from the JSON file and reload them into the storage dictionary."""
        try:
            with open(self.__file_path, 'r') as f:
                loaded_objs = json.load(f)
                for key, val in loaded_objs.items():
                    class_name, obj_id = key.split('.')
                    module = __import__('models.' + class_name, fromlist=[class_name])
                    cls = getattr(module, class_name)
                    obj = cls(**val)
                    self.__objects[key] = obj
        except FileNotFoundError:
            pass
