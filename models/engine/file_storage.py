#!/usr/bin/python3
"""
Module defining FileStorage class.
"""

import json
from models.base_model import BaseModel
from models.user import User


class FileStorage:
    """
    Serializes and deserializes JSON file to instances.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary __objects.
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Sets in __objects the obj with key <obj class name>.id.
        """
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file (__file_path).
        """
        obj_dict = {}
        for key, obj in FileStorage.__objects.items():
            obj_dict[key] = obj.to_dict()
        with open(FileStorage.__file_path, 'w') as file:
            json.dump(obj_dict, file)

    def reload(self):
        """
        deserializes the JSON file to __objects
        """
        current_classes = {
            'BaseModel': BaseModel,
            'User': User
            }

        if not os.path.exists(self.__file_path):
            return

        with open(self.__file_path, 'r') as file:
            deserialized = None

            try:
                deserialized = json.load(file)
            except json.JSONDecodeError:
                pass

            if deserialized is None:
                return

            self.__objects = {
                k: current_classes[k.split('.')[0]](**v)
                for k, v in deserialized.items()}
