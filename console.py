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
    
    def __getattr__(self, attr):
        """Custom attribute getter to enable ClassName.all() syntax"""
        class_name = attr.split(".")[0]
        if class_name in self.options:
            return lambda: self.do_all(class_name)
        else:
            raise AttributeError(f"'HBNBCommand' object has no attribute '{attr}'")
   
    def default(self, line):
        """Handles the ClassName.all() syntax"""
        tokens = line.split('.')
        if len(tokens) == 2 and tokens[1] == 'all()':
            class_name = tokens[0]
            if class_name in self.options:
                self.do_all(class_name)
                return
        super().default(line)


    def do_create(self, arg):
        """ Create a new instance """
        if len(arg) == 0:
            print('** class name missing **')
            return
        if arg:
            arg_list = arg.split()
            if len(arg_list) == 1:
                if arg in self.options.keys():
                    new_obj = self.options[arg]()
                    new_obj.save()
                    print(new_obj.id)
                else:
                    print("** class doesn't exist **")

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

    # def do_all(self, args):
    #     """ Prints all string representation of all
    #     instances based or not on the class name. """
    #     if len(args) == 0:
    #         print([str(a) for a in storage.all().values()])
    #     elif args not in self.options:
    #         print("** class doesn't exist **")
    #     else:
    #         print([str(a) for b, a in storage.all().items() if args in b])
    
    def do_all(self, args):
        """Prints all string representation of all
        instances based or not on the class name."""
        if args and args in self.options:
            class_name = args
            instances = storage.all()
            filtered_instances = [str(obj) for obj in instances.values() if isinstance(obj, self.options[class_name])]
            print(filtered_instances)
        elif args and args not in self.options:
            print("** class doesn't exist **")
        else:
            print([str(obj) for obj in storage.all().values()])



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

    # def do_count(self, args):
    #     """Usage: count <class> or <class>.count()
    #     Retrieve the number of instances of a given class."""
    #     # argl = shlex.split(arg)
    #     # count = 0
    #     # for obj in storage.all().values():
    #     #     if argl[0] == obj.__class__.__name__:
    #     #         count += 1
    #     # print(count)
    #     args = shlex.split(args)
    #     my_dict = storage.all()
    #     appearances = [
    #         appearance for appearance in my_dict if 
    #         appearance.startswith("." + args[0])
    #     ]
    #     print(len(appearances))

if __name__ == "__main__":
    HBNBCommand().cmdloop()
