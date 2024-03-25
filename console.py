#!/usr/bin/python3
import cmd
from models import storage
from models.user import User

class HBNBCommand(cmd.Cmd):
    """Class for the command-line interpreter."""

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """Handle EOF signal."""
        print('')
        return True

    def emptyline(self):
        """Called when an empty line is entered."""
        pass

    def create(self, arg):
        """Create command to create a new instance of a class.

        Args:
            arg (str): Arguments passed along with the create command.
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in storage.classes():
            print("** class doesn't exist **")
            return
        new_instance = storage.classes()[class_name]()
        for param in args[1:]:
            key, value = param.split('=')
            setattr(new_instance, key, value)
        new_instance.save()
        print(new_instance.id)

    def show(self, arg):
        """Show command to display information about an instance.

        Args:
            arg (str): Arguments passed along with the show command.
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in storage.classes():
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)
        if key in storage.all():
            print(storage.all()[key])
        else:
            print("** no instance found **")

    def destroy(self, arg):
        """Destroy command to delete an instance.

        Args:
            arg (str): Arguments passed along with the destroy command.
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in storage.classes():
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)
        if key in storage.all():
            del storage.all()[key]
            storage.save()
        else:
            print("** no instance found **")

    def all(self, arg):
        """All command to display all instances of a class.

        Args:
            arg (str): Arguments passed along with the all command.
        """
        args = arg.split()
        if args and args[0] not in storage.classes():
            print("** class doesn't exist **")
            return
        instances = [str(v) for k, v in storage.all().items() if not args or k.split('.')[0] == args[0]]
        print(instances)

    def update(self, arg):
        """Update command to update attributes of an instance.

        Args:
            arg (str): Arguments passed along with the update command.
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in storage.classes():
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)
        if key not in storage.all():
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        attribute_name = args[2]
        attribute_value = args[3]
        obj = storage.all()[key]
        setattr(obj, attribute_name, attribute_value)
        obj.save()

if __name__ == "__main__":
    HBNBCommand().cmdloop()
