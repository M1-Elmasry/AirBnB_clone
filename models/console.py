#!/usr/bin/python3

import cmd
import base_model
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

    def help_quit(self):
        """
        Display help information for the 'quit' command.
        """
        print("quit command to exit the interpreter")
        print("Usage: quit")

    def help_EOF(self):
        """
        Display help information for the 'EOF' command.
        """
        print("EOF command to exit the interpreter")
        print("Usage: EOF")

    def emptyline(self):
        """
        Do nothing when an empty line is entered.
        """
        pass

    def default(self):
        """
        Do nothing for unrecognized commands.
        """
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
