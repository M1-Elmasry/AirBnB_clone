#!/usr/bin/python3

import cmd
from models.base_model import BaseModel
from models.user import User
from models import storage
import readline
import sys



class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand - Python Console for HBNB Project

    This class implements a simple command-line interpreter for the HBNB project.
    Users can interact with the interpreter to perform various commands.

    Attributes:
        prompt (str): The command prompt for the interpreter.
        doc_header (str): Header for documented commands.
        misc_header (str): Header for additional information.
        ruler (str): The character used to create separation lines in the help output.
    """

    prompt = "(hbnb) "
    doc_header = "Documented commands (type help <topic>):"
    misc_header = "Additional Information"
    ruler = "="

    __classes = {"BaseModel": BaseModel, "User": User}

    @classmethod
    def classes(cls):
        """ getter of __classes to can use it in other modules """
        return HBNBCommand.__classes

    def do_quit(self, args):
        """
        Quit the interpreter.

        This command allows the user to exit the interpreter gracefully.

        Args:
            args (str): Any additional arguments passed with the command.

        Returns:
            bool: True to exit the interpreter.
        """
        print("Quitting")
        return True

    def help_quit(self):
        """
        Display help information for the 'quit' command.
        """
        print("quit command to exit the interpreter")
        print("Usage: quit")

    def do_EOF(self, args):
        """
        Quit the interpreter.

        This command allows the user to exit the interpreter gracefully using the EOF (End of File) input.

        Args:
            args (str): Any additional arguments passed with the command.

        Returns:
            bool: True to exit the interpreter.
        """
        print("Quitting")
        return True

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
        Prints the string representation of an instance based on the class name and id
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
            all_objects_stored = storage.all()
            id = splitted_args[1]
            key = f"{class_name}.{id}"
            obj_str = all_objects_stored[key]
            print(obj_str)
        except KeyError:
            print("** no instance found **")
            return

    def help_show(self):
        """
        Display help information for the 'show' command.
        """
        print(
            "Prints the string representation of an instance based on the class name and id"
        )
        print("Usage: show <class> <id>")

    def do_destroy(self, args):
        """
        Deletes an instance based on the class name and id (save the change into the JSON file).
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
        print(
            "Deletes an instance based on the class name and id (save the change into the JSON file)"
        )
        print("Usage: show <class> <id>")

    def do_all(self, args):
        """
        Prints all string representation of all instances based or not on the class name.
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
                print("* class doesn't exist **")
                return

    def help_all(self):
        """
        Display help information for the 'all' command.
        """
        print(
            "Prints all string representation of all instances based or not on the class name."
        )
        print("Usage: `all <class>` or `all`")

    def do_update(self, args):
        """
        Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file)
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
            print("* value missing **")
            return

        try:
            # if the attribute already exists in the object
            attr_type = type(getattr(needed_obj, splitted_args[2]))
            new_value = attr_type(" ".join(splitted_args[3:]).strip("'\""))
            setattr(needed_obj, splitted_args[2], new_value)
            needed_obj.save()
        except AttributeError:
            # if the attribute does'nt exists in the object
            setattr(
                needed_obj, splitted_args[2], " ".join(splitted_args[3:]).strip("'\"")
            )
            needed_obj.save()

    def help_update(self):
        """
        Display help information for the 'update' command.
        """
        print(
            "Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file)"
        )
        print("Usage: update <class> <id> <attribute> <value>")

    def emptyline(self):
        """
        Do nothing when an empty line is entered.
        """
        pass

    def default(self, args):
        """
        Do nothing for unrecognized commands.
        """


if __name__ == "__main__":
    HBNBCommand().cmdloop()
