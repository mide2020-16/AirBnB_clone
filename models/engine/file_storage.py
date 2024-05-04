#!/usr/bin/python3
"""
    This is the engine created for storing instance in the form of json string for persistency
"""
import json
import os

class FileStorage:
    """FileStorage class for managing serialization and deserialization of objects to/from JSON file."""
    def __init__(self, file_path='file.json'):
        self.__file_path = file_path
        self.__objects = {}


    def all(self):
        """Retrieve all stored objects."""
        return self.__objects

    def new(self, obj):
        """
        Add a new object to the storage dictionary."""
        key = self.__generate_key(obj)
        self.__objects[key] = obj.to_dict()

    def save(self):
        """
        Serialize objects and save them to the JSON file.
        """
        with open(self.__file_path, 'w') as f:
            json.dump(self.__objects, f)

    def reload(self):
        """
        Deserialize objects from the JSON file and reload them into the storage dictionary.
        """

        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as f:
                self.__objects = json.load(f)

    def __generate_key(self, obj):
        """Generate a key for the object."""
        return f"{obj.__class__.__name__}.{obj.id}"

    def classes(self):
        classes = {}
        for key, value in self.all().items():
            classes[key] = value
        return classes
