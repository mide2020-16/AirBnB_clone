#!/usr/bin/env python3
"""
This is the command interpreter for managing
instances of BaseModel
"""

import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from sys import stdin
from models.user import User


class HBNBCommand(cmd.Cmd):
    """
    Command interpreter class for managing instances
    """


    prompt = "(hbnb) "
    storage = FileStorage()
    storage.reload()

    if stdin.isatty() is False:
        prompt = "(hbnb) \n"

    def __init__(self):
        """Initialise console"""
        super().__init__()


    def do_create(self, arg):
        """Creeates a new instance of BaseModel"""
        if not arg:
            print("** class name missing **")
            return

        try:
            obj = eval(arg)()
            obj.save()
            print(obj.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """prints the string representation of an instance based on the class name and id"""

        args = arg.split()
        class_name = args[0]
        instance_key = "{}.{}".format(class_name, args[1])
        objects = self.storage.all()
        self.class_name_validator(arg)

        print(objects[instance_key])

    def do_destroy(self, arg):
        """Destroy an instance of based on the class name and id and save changes"""

        args = arg.split()
        class_name = args[0]
        instance_key = "{}.{}".format(class_name, args[1])
        objects = self.storage.all()
        self.class_name_validator()

        del objects[instance_key]
        self.storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances based or not class name"""

        class_name = None
        if arg:
            class_name = arg.split()[0]
            if class_name not in self.storage.classes():
                print("** class doesn't exist **")
                return
        objects = self.storage.all()
        if class_name:
            objects = {k: v for k, v in objects.items() if k.split('.')[0] == class_name}

        print([str(v) for v in objects.values()])

    def do_update(self, arg):
        """Updates the engine for an instance added or removed"""

        args = arg.split()
        objects = self.storage.all()
        class_name = args[0]
        instance_key = "{}.{}".format(class_name, args[1])

        self.class_name_validator()
        if len(args) < 4:
            print("** attribute name missing **")
            return

        attr_name = args[2]
        if len(args) < 5:
            print("** value missing **")
            return
        attr_value = args[3]

        if hasattr(objects[instance_key], attr_name):
            setattr(objects[instance_key], attr_name, attr_value)
            objects[instance_key].save()
        else:
            print("** attribute doesn't exist **")

    def class_name_validator(self, arg):
        """Validates the presence of an instance  and it's id"""

        args = arg.split()
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in self.storage.classes():
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_key = "{}.{}".format(class_name, args[1])
        objects = self.storage.all()
        if instance_key not in objects:
            print("** no instance found **")

    def emptyline(self):
        """Emptyline entered"""

        pass

    def do_help(self, arg):
        """Help for console"""

        return super().do_help(arg)

    def do_quit(self, arg):
        """Quit console"""

        return True

    def do_EOF(self, arg):
        """End of file of a console"""

        return True


if __name__ == "__main__":
    HBNBCommand().cmdloop()
