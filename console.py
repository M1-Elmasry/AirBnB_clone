#!/usr/bin/python3
"""
This module implements a Python Console for the AirBnB Project.

It provides a command-line interpreter for interact with
the AirBnB project by performing various commands.

The commands provided by this module include creating new instances,
displaying information about instances, updating attributes, and more.

It utilizes classes and modules from the AirBnB project
to manage and manipulate data.

This module is designed to work with the AirBnB project's data models,
such as BaseModel, User, City, Place, Review, State, and Amenity,
and uses the storage module to manage data storage and retrieval.
"""

import re
import sys
import cmd
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand - Python Console for HBNB Project

    This class implements a simple command-line interpreter.
    Users can interact with the interpreter to perform various commands.

    Attributes:
        prompt (str): The command prompt for the interpreter.
        doc_header (str): Header for documented commands.
        misc_header (str): Header for additional information.
        ruler (str): The character used to create
        separation lines in the help output.
    """

    prompt = "(hbnb) " if sys.stdin.isatty() else ""
    doc_header = "Documented commands (type help <topic>):"
    misc_header = "Additional Information"
    ruler = "="

    __classes = {
        "BaseModel": BaseModel,
        "User": User,
        "City": City,
        "Place": Place,
        "Review": Review,
        "State": State,
        "Amenity": Amenity,
    }
    __types = {
        "name": str,
        "stat_id": str,
        "city_id": str,
        "user_id": str,
        "description": str,
        "number_rooms": int,
        "number_bathrooms": int,
        "max_guest": int,
        "price_by_night": int,
        "latitude": float,
        "longitude": float,
        "place_id": str,
        "text": str,
    }

    @classmethod
    def classes(cls):
        """getter of __classes to can use it in other modules"""
        return HBNBCommand.__classes

    def do_quit(self, args):
        """
        Quit the interpreter.
        This command allows the user to exit the interpreter gracefully.
        """
        exit()

    def help_quit(self):
        """
        Display help information for the 'quit' command.
        """
        print("quit command to exit the interpreter")
        print("Usage: quit")

    def do_EOF(self, args):
        """
        Quit the interpreter.
        This command allows the user to exit the interpreter
        gracefully using the EOF (End of File) input.
        """
        exit()

    def help_EOF(self):
        """
        Display help information for the 'EOF' command.
        """
        print("EOF command to exit the interpreter")
        print("Usage: EOF")

    def do_create(self, args):
        """
        Creates a new instance of specific class (first word in @args),
        and saves it (to the JSON file) and prints it's id
        ex: create <class_name>

        Args:
            args (str): Any additional arguments passed with the command.
        """
        if len(args) == 0:
            print("** class name missing **")
            return

        splitted_args = args.split(" ")

        try:
            new_instance = HBNBCommand.__classes[splitted_args[0]]()
            print(new_instance.id)
            new_instance.save()
        except KeyError:
            print("** class doesn't exist **")

    def help_create(self):
        """
        Display help information for the 'create' command.
        """
        print("creates new instances from specific class and store it")
        print("Usage: create <class>")

    def do_show(self, args):
        """
        Prints the string representation of an instance based on
        the class name and id
        ex: show <class> <id>

        Args:
            args (str): Any additional arguments passed with the command.
        """
        splitted_args = args.split(" ")
        len_spltd_args = len(splitted_args)

        if splitted_args[0] == "":
            print("** class name missing **")
            return

        # make exception handling instead of iterate over
        # `self.classes.keys()` and check if class valid or not
        try:
            class_name = splitted_args[0]
            HBNBCommand.__classes[class_name]
        except KeyError:
            print("** class doesn't exist **")
            return

        if len_spltd_args < 2:
            print("** instance id missing **")
            return

        try:
            all_stored_objects = storage.all()
            id = splitted_args[1]
            key = f"{class_name}.{id}"
            obj_str = all_stored_objects[key]
            print(obj_str)
        except KeyError:
            print("** no instance found **")
            return

    def help_show(self):
        """
        Display help information for the 'show' command.
        """
        print("Prints the str repr of an instance")
        print("based on the class name and id")
        print("Usage: show <class> <id>")

    def do_destroy(self, args):
        """
        Deletes an instance based on the class name and id
        (and save the changes).
        Ex: destroy <class> <id>

        Args:
            args (str): Any additional arguments passed with the command.
        """
        splitted_args = args.split(" ")
        len_spltd_args = len(splitted_args)

        if splitted_args[0] == "":
            print("** class name missing **")
            return

        # make exception handling instead of iterate over
        # `self.classes.keys()` and check if class valid or not
        try:
            class_name = splitted_args[0]
            HBNBCommand.__classes[class_name]
        except KeyError:
            print("** class doesn't exist **")
            return

        if len_spltd_args < 2:
            print("** instance id missing **")
            return

        try:
            id = splitted_args[1]
            key = f"{class_name}.{id}"
            del storage.all()[key]
            storage.save()
        except KeyError:
            print("** no instance found **")
            return

    def help_destroy(self):
        """
        Display help information for the 'destroy' command.
        """
        print("Deletes an instance based on the")
        print("class name and id (and save the changes)")
        print("Usage: show <class> <id>")

    def do_all(self, args):
        """
        Prints all string representation of all
        instances based or not on the class name.
        Ex: `all BaseModel` or `all`.
        """
        splitted_args = args.split(" ")
        objects = storage.all()

        if splitted_args[0] == "":
            print([str(objects[i]) for i in objects.keys()])
        else:
            try:
                class_name = splitted_args[0]
                HBNBCommand.__classes[class_name]
                print(
                    [
                        str(objects[i])
                        for i in objects.keys()
                        if i.startswith(class_name)
                    ]
                )
            except KeyError:
                print("** class doesn't exist **")
                return

    def help_all(self):
        """
        Display help information for the 'all' command.
        """
        print("Prints all string representation of")
        print("all instances based or not on the class name.")
        print("Usage: `all <class>` or `all`")

    def do_update(self, args):
        """
        Updates an instance based on the class name and id by
        adding or updating attribute (and save the changes)
        Ex: update <class> <id> <attribute> <value>

        Args:
            args (str): Any additional arguments passed with the command.
        """
        splitted_args = args.split(" ")
        len_spltd_args = len(splitted_args)

        if splitted_args[0] == "":
            print("** class name missing **")
            return

        # make exception handling instead of iterate over
        # `self.classes.keys()` and check if class valid or not
        try:
            class_name = splitted_args[0]
            HBNBCommand.__classes[class_name]
        except KeyError:
            print("** class doesn't exist **")
            return

        if len_spltd_args < 2:
            print("** instance id missing **")
            return

        try:
            id = splitted_args[1]
            key = f"{class_name}.{id}"
            needed_obj = storage.all()[key]
        except KeyError:
            print("** no instance found **")
            return

        if len_spltd_args < 3:
            print("** attribute name missing **")
            return

        if len_spltd_args < 4:
            print("** value missing **")
            return

        attr_name = splitted_args[2]
        attr_value = splitted_args[3:]

        try:
            # if the attribute already exists in the object
            # the error may raises from below line
            attr_type = type(getattr(needed_obj, attr_name))
            # if the value of the attribute
            # like this > "value" or 'value'
            # (the string include single/double qoutes)
            # remove single/double qoutes
            casted_attr_value = attr_type(" ".join(attr_value).strip("'\""))
            # set the new attr and save it
            setattr(needed_obj, attr_name, casted_attr_value)
            needed_obj.save()
        except AttributeError:
            try:
                # if the attribute does'nt exists in the object
                # and type exists in (HBNBCommand.__types)
                attr_type = HBNBCommand.__types[attr_name]
                setattr(
                    needed_obj,
                    attr_name,
                    attr_type(" ".join(attr_value).strip("'\"")),
                )
                needed_obj.save()
            except KeyError:
                # if the attr not exists in the object
                # and the name of it not exists in (HBNBCommand.__types)
                setattr(
                    needed_obj,
                    attr_name,
                    " ".join(attr_value).strip("'\""),
                )
                needed_obj.save()

    def help_update(self):
        """
        Display help information for the 'update' command.
        """
        print("Updates an instance based on the class name and id")
        print("by adding or updating attribute")
        print("Usage: update <class> <id> <attribute> <value>")

    def do_count(self, args):
        """
        write docs
        """
        splitted_args = args.split(" ")
        objects = storage.all()

        if splitted_args[0] == "":
            print("** class name missing **")
            return
        else:
            try:
                cls_name = splitted_args[0]
                HBNBCommand.__classes[cls_name]
                print(
                    "{}".format(
                        len(
                            [
                                1
                                for i in objects.keys()
                                if i.startswith(f"{cls_name}")
                            ]
                        )
                    )
                )
            except KeyError:
                print("** class doesn't exist **")
                return

    def emptyline(self):
        """
        Do nothing when an empty line is entered.
        """
        pass

    def default(self, args):
        """
        Do for unrecognized commands.
        """
        methods = ["update", "all", "show", "create", "destroy", "count"]
        # match syntax like this "<class>.<method>(<args>)"
        # method should from @methods
        pattern = r"^([a-zA-Z0-9]*)\.(" + "|".join(methods) + r")\((.*)\)$"
        match = re.match(pattern, args)
        if match:
            class_name = match.group(1)
            method_name = match.group(2)
            input_args = match.group(3)
            HBNBCommand().onecmd(f"{method_name} {class_name} {input_args}")
        else:
            pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
