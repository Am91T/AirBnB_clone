#!/usr/bin/python3
"""Module defining HBNBCommand class for the command interpreter."""

import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.review import Review
from models.amenity import Amenity
from models.place import Place


class HBNBCommand(cmd.Cmd):
    """Command interpreter class."""

    prompt = "(hbnb) "
    __classes = {
        "BaseModel": BaseModel,
        "User": User,
        "Amenity": Amenity,
        "City": City,
        "Place": Place,
        "State": State,
        "Review": Review
    }

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """Exit the program when EOF is reached."""
        print()
        return True

    def emptyline(self):
        """Do nothing when an empty line is entered."""
        pass

    def help_quit(self):
        """Print help message for quit command."""
        print("Quit command to exit the program\n")

    def help_EOF(self):
        """Print help message for EOF command."""
        print("Exit the program when EOF is reached\n")

    def do_create(self, arg):
        """Creates a new instance of BaseModel."""
        if not arg:
            print("** class name missing **")
        elif arg not in self.__classes:
            print("** class doesn't exist **")
        else:
            new_instance = self.__classes[arg]()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """Prints the string of an instance."""
        args = arg.split()
        if not arg:
            print("** class name missing **")
        elif args[0] not in self.__classes:
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
        """Deletes an instance."""
        args = arg.split()
        if not arg:
            print("** class name missing **")
        elif args[0] not in self.__classes:
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
        Prints all string of all instances.
        """
        args = arg.split()
        all_objs = storage.all()
        if not arg:
            print([str(obj) for obj in all_objs.values()])
        elif args[0] not in self.__classes:
            print("** class doesn't exist **")
        else:
            result = []
            for key, obj in all_objs.items():
                if key.split('.')[0] == args[0]:
                    result.append(obj)
                print(result)

    def do_update(self, arg):
        """Updates an instance."""
        args = arg.split()
        all_objs = storage.all()
        if not arg:
            print("** class name missing **")
        elif args[0] not in self.__classes:
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
