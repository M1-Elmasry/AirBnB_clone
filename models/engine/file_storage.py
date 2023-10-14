#!/usr/bin/python3
"""
representing a FileStorage Class

This module defines the `FileStorage` class,
which is responsible for serializing objects to json objects,
storing json objects, deserializing json objects
"""
import json


class FileStorage:
    """
    FileStorage class responsible for serializing objects to JSON format,
    storing JSON objects, and deserializing JSON objects.

    Class Attributes:
        __file_path (str): The path to the JSON file where objects are stored.
        __objects (dict): A dictionary that holds objects in memory.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Return a dictionary containing all objects currently loaded in memory.
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Adds a new object to the in-memory dictionary __objects.

        Args:
            obj (BaseModel): The object to be added to the dictionary.
        """
        class_name = obj.__class__.__name__
        self.all()[f"{class_name}.{obj.id}"] = obj

    def save(self):
        """
        Serializes and saves all objects in __objects
        to a JSON file (__file_path).
        """
        serialized_objects = {}
        for k, v in self.all().items():
            serialized_objects[k] = v.to_dict()

        with open(FileStorage.__file_path, "w") as file:
            json.dump(serialized_objects, file)

    def reload(self):
        """
        Loads objects from the JSON file (__file_path)
        into memory and deserializes them
        into their respective object instances.
        This method is typically called when the program starts
        to populate the __objects dictionary with data from the file.
        """
        try:
            with open(FileStorage.__file_path, "r") as file:
                from console import HBNBCommand

                temp = json.load(file)
                # we should return the dict object
                # (the values of keys in the temp dict) to BaseModel objects
                # the loaded objects will be like This
                # {<class_name>.id: {created_at:..., updated_at:...., ...}}
                # and we want to return the value to object to be like This
                # {<class_name>.id: obj}
                # why ?,
                # because when add new objs to `__objects` and want to save it
                # with above save method it iterate over `__objects`
                # and call to_dict() method
                # if we didn't return the values to BaseModel object
                # we will acts like This
                # {created_at:..., ...}.to_dict() and this will raise error
                # because dict object deos'nt have to_dict() method,
                # the owner of to_dict method is BaseModel, got it?
                for key, value in temp.items():
                    cls_name = key.split(".")[0]
                    self.all()[key] = HBNBCommand.classes()[cls_name](**value)
        except FileNotFoundError:
            pass
