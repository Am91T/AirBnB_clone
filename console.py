#!/usr/bin/python3
"""Defines the HBnB console."""
import cmd


class HBNBCommand(cmd.Cmd):
    """Defines the HolbertonBnB command interpreter.
    Attributes:
        prompt (str): The command prompt.
    """
    prompt = '(hbnb) '

    def emptyline(self):
        """Do nothing when an empty line is entered"""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program when EOF is reached"""
        print()
        return True

    def help_quit(self):
        """Help message for quit command"""
        print("Quit command to exit the program")

    def help_EOF(self):
        """Help message for EOF (Ctrl+D)"""
        print("Exit the program")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
