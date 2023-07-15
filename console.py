#! /usr/bin/python3
"""console"""
import cmd
import shlex
import sys
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.review import Review
from models.place import Place
from models.city import City
from models.amenity import Amenity


sys.path.append("/home/njuguna/Desktop/alx/SEfoundations/AirBnB_clone/models")


class HBNBCommand(cmd.Cmd):
    """console class"""
    prompt = "(hbnb) "
    options = {"BaseModel": BaseModel,
               "Amenity": Amenity,
               "City": City,
               "Place": Place,
               "Review": Review,
               "State": State,
               "User": User
               }

    def do_quit(self, arg):
        """Quit command to exit the program"""
        exit()

    def do_EOF(self, arg):
        """implement end of file an exit"""
        print()
        exit()

    def emptyline(self):
        """empty line"""
        pass

    def do_create(self, args):
        """creates a new instance of BaseModel"""
        args = shlex.split(args)
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] in self.options:
            implementation = self.options[args[0]]
        else:
            print("** class doesn't exist **")
            return
        print(implementation.id)
        BaseModel.save()
        
                    

    def do_show(self, args):
        """Prints the string representation of an instance
        based on the class name and id"""
        args = shlex.split(args)
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] in self.options:
            if len(args) > 1:
                arg_id = f"{args[0]}.{args[1]}"
                if arg_id in storage.all():
                    print(storage.all()[arg_id])
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")
            

    def do_destroy(self, args):
        """ Deletes an instance based on the class name and id"""
        args = shlex.split(args)
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] in self.options:
            if len(args) > 1:
                args_id = f"{args[0]}.{args[1]}"
                if args_id in storage.all():
                    storage.all().pop(args_id)
                    storage.save()
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")
            

    def do_all(self, args):
        """ Prints all string representation of all
        instances based or not on the class name. """
        args = shlex.split(args)
        if len(args) == 0:
            print([str(a) for a in storage.all().values()])
        elif args[0] not in self.options:
            print("** class doesn't exist **")
        else:
            print([str(a) for b, a in storage.all().items() if args in b])

    def do_update(self, arg):
        """ updates an instance"""
        arg = arg.split()
        if len(arg) == 0:
            print('** class name missing **')
        elif arg[0] not in self.options:
            print("** class doesn't exist **")
        elif len(arg) == 1:
            print('** instance id missing **')
        else:
            key = arg[0] + '.' + arg[1]
            if key in storage.all():
                if len(arg) > 2:
                    if len(arg) == 3:
                        print('** value missing **')
                    else:
                        setattr(
                            storage.all()[key],
                            arg[2],
                            arg[3][1:-1])
                        storage.all()[key].save()
                else:
                    print('** attribute name missing **')
            else:
                print('** no instance found **')

    def do_count(self, arg):
        """Usage: count <class> or <class>.count()
        Retrieve the number of instances of a given class."""
        argl = arg.split()
        count = 0
        for obj in storage.all().values():
            if argl[0] == obj.__class__.__name__:
                count += 1
        print(count)
        

if __name__ == "__main__":
    HBNBCommand().cmdloop()
