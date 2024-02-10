#!/usr/bin/python3
"""This module defines the HBnB console."""
import cmd


class HBNBCommand(cmd.Cmd):
    """This class defines the alxBnB command interpreter.
    Attributes:
        prompt (str): The command prompt.
    """
    prompt = '(hbnb) '

    def emptyline(self):
        """Do nothing when an empty line is entered"""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program
        Args:
            arg (str): Arguments passed to the command (ignored).
        Returns:
            bool: True to exit the program.
        """
        return True

    def do_EOF(self, arg):
        """Exit the program when EOF is reached
        Args:
            arg (str): Arguments passed to the command (ignored).
        """
        print()
        return True

    def help_quit(self):
        """Provide help message for quit command"""
        print("Quit command to exit the program")

    def help_EOF(self):
        """Provide help message for EOF (Ctrl+D)"""
        print("Exit the program")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
