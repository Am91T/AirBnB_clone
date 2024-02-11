#!/usr/bin/python3
"""
Module defining HBNBCommand class for the command interpreter.
"""

import cmd
from models.base_model import BaseModel
from models import storage

class HBNBCommand(cmd.Cmd):
    """
    Command interpreter class.
    """

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """
        Quit command to exit the program.
        """
        return True

    def do_EOF(self, arg):
        """
        Exit the program when EOF is reached.
        """
        print()
        return True

    def emptyline(self):
        """
        Do nothing when an empty line is entered.
        """
        pass

    def help_quit(self):
        """
        Print help message for quit command.
        """
        print("Quit command to exit the program\n")

    def help_EOF(self):
        """
        Print help message for EOF command.
        """
        print("Exit the program when EOF is reached\n")

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel, saves it, and prints the id.
        """
        if not arg:
            print("** class name missing **")
        elif arg not in globals():
            print("** class doesn't exist **")
        else:
            new_instance = globals()[arg]()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """
        Prints the string representation of an instance.
        """
        args = arg.split()
        if not arg:
            print("** class name missing **")
        elif args[0] not in globals():
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            all_objs = storage.all()
            if key not in all_objs:
                print("** no instance found **")
            else:
                print(all_objs[key])

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id.
        """
        args = arg.split()
        if not arg:
            print("** class name missing **")
        elif args[0] not in globals():
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            all_objs = storage.all()
            if key not in all_objs:
                print("** no instance found **")
            else:
                del all_objs[key]
                storage.save()

    def do_all(self, arg):
        """
        Prints all string representations of all instances.
        """
        args = arg.split()
        all_objs = storage.all()
        if not arg:
            print([str(obj) for obj in all_objs.values()])
        elif args[0] not in globals():
            print("** class doesn't exist **")
        else:
            print([str(obj) for key, obj in all_objs.items() if key.split('.')[0] == args[0]])

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id by adding or updating attribute.
        """
        args = arg.split()
        all_objs = storage.all()
        if not arg:
            print("** class name missing **")
        elif args[0] not in globals():
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            key = args[0] + "." + args[1]
            if key not in all_objs:
                print("** no instance found **")
            else:
                obj = all_objs[key]
                setattr(obj, args[2], args[3])
                obj.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
