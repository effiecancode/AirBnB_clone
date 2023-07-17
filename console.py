#! /usr/bin/python3
"""my console"""
import cmd
import shlex
import ast
import os
import sys
fpath = os.path.join(os.path.dirname(__file__), 'models')
sys.path.append(fpath)
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.review import Review
from models.place import Place
from models.city import City
from models.amenity import Amenity

from models import storage


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
        """Custom attribute getter to enable ClassName.function() syntax"""
        class_name = attr.split(".")[0]
        if class_name in self.options:
            if attr.endswith('.all()'):
                return lambda: self.do_all(class_name)
            elif attr.endswith('.destroy'):
                return lambda id: self.do_destroy(f"{class_name} {id}")
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

        """Handles the ClassName.count() syntax"""
        if len(tokens) == 2 and tokens[1] == 'count()':
            class_name = tokens[0]
            if class_name in self.options:
                count = sum(1 for obj in storage.all().values()
                            if isinstance(obj, self.options[class_name]))
                print(count)
                return
        super().default(line)

        """Handles the ClassName.show(id) syntax"""
        if len(tokens) == 2 and tokens[1].startswith('show('):
            if tokens[1].endswith(')'):
                class_name = tokens[0]
                if class_name in self.options:
                    instance_id = tokens[1][5:-1]
                    self.do_show(f"{class_name} {instance_id}")
                    return
        super().default(line)

        """Handles the ClassName.destroy(id) syntax"""
        if len(tokens) == 2 and tokens[1].startswith('destroy('):
            if tokens[1].endswith(')'):
                class_name = tokens[0]
                if class_name in self.options:
                    instance_id = tokens[1][8:-1]
                    self.do_destroy(f"{class_name} {instance_id}")
                    return
        super().default(line)

        """Handles the ClassName.update(id, attribute, value) syntax"""
        if len(tokens) == 2 and tokens[1].startswith('update('):
            if tokens[1].endswith(')'):
                cls_name = tokens[0]
                if cls_name in self.options:
                    update_tokens = tokens[1][7:-1].split(', ')
                    if len(update_tokens) == 3:
                        inst_id = update_tokens[0]
                        attr_name = update_tokens[1]
                        attr_val = update_tokens[2]
                        m_upd = f"{cls_name} {inst_id} {attr_name} {attr_val}"
                        self.do_update(m_upd)
                        return
        super().default(line)

        """Handles the ClassName.update(id, dictionary_rep) syntax"""
        if len(tokens) == 2 and tokens[1].startswith('update('):
            if tokens[1].endswith(')'):
                class_name = tokens[0]
                if class_name in self.options:
                    update_tokens = tokens[1][7:-1].split(', ', 1)
                    if len(update_tokens) == 2:
                        inst_id = update_tokens[0]
                        dictionary_repr = update_tokens[1]
                        try:
                            attr_dict = ast.literal_eval(dictionary_repr)
                            my_update = f"{class_name} {inst_id}", attr_dict
                            self.do_update(my_update)
                            return
                        except (ValueError, SyntaxError):
                            pass
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
                arg_id = args[1]
                class_name = args[0]
                instance_key = f"{class_name}.{arg_id}"
                instances = storage.all()
                if instance_key in instances:
                    print(instances[instance_key])
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_destroy(self, args):
        """Deletes an instance based on the class name and id"""
        args = shlex.split(args)
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] in self.options:
            if len(args) > 1:
                arg_id = args[1]
                class_name = args[0]
                instance_key = f"{class_name}.{arg_id}"
                instances = storage.all()
                if instance_key in instances:
                    del instances[instance_key]
                    storage.save()
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_all(self, args):
        """Prints all string representation of all
        instances based or not on the class name."""
        if args and args in self.options:
            class_name = args
            instances = storage.all()
            filtered_instances = [str(obj) for obj in instances.values()
                                  if isinstance(obj, self.options[class_name])]
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

    def do_count(self, arg):
        """Retrieve the number of instances of a given class"""
        arg_list = arg.split()
        if len(arg_list) == 1:
            class_name = arg_list[0]
            if class_name in self.options:
                count = sum(1 for obj in storage.all().values()
                            if isinstance(obj, self.options[class_name]))
                print(count)
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
