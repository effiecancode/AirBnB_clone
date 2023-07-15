#! /usr/bin/python3
"""console"""
import cmd

from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """console class"""
    prompt = "(hbnb) "
    options = {"BaseModel":BaseModel}

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
        if args:
            args_list = args.split()
            if len(args_list) == 1:
                if args in self.options.keys():
                    new_obj = self.options[args]()
                    new_obj.save()
                    print(new_obj.id)
                else:
                    print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_show(self, args):
        """Prints the string representation of an instance 
        based on the class name and id"""
        my_dict = storage.all()
        if args:
            args_list = args.split()
            if args_list[0] not in self.options.keys():
                print("** class doesn't exist **")
            elif len(args_list) == 1:
                print("** instance id missing **")
            elif f"{args_list[0]}.{args_list[1]}" not in my_dict:
                print("** no instance found **")
            else:
                print(my_dict[f"{args_list[0]}.{args_list[1]}"])
        else:
            print("** class name missing **")

    def do_destroy(self, args):
        """ Deletes an instance based on the class name and id"""
        if args:
            arg_list = args.split()
            try:
                obj = eval(arg_list[0])
            except Exception:
                print("** class doesn't exist **")
            if len(arg_list) == 1:
                print('** instance id missing **')
            if len(arg_list) > 1:
                key = arg_list[0] + '.' + arg_list[1]
                if key in storage.all():
                    storage.all().pop(key)
                    storage.save()
                else:
                    print('** no instance found **')
        else:
            print("** class name missing **")


    def do_all(self, args):
        """ Prints all string representation of all 
        instances based or not on the class name. """
        if len(args) == 0:
            print([str(a) for a in storage.all().values()])
        elif args not in self.classes:
            print("** class doesn't exist **")
        else:
            print([str(a) for b, a in storage.all().items() if args in b])

    def do_update(self, arg):
        """ updates an instance"""
        arg = arg.split()
        if len(arg) == 0:
            print('** class name missing **')
        elif arg[0] not in self.classes:
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




if __name__ == "__main__":
    HBNBCommand().cmdloop()