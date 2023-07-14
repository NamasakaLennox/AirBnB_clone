#!/usr/bin/python3
"""
A module that contains the console
"""
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
import cmd
from models.place import Place
from models.state import State
from models.review import Review
from models import storage
from models.user import User


class HBNBCommand(cmd.Cmd):
    """
    A cmd interpretor class\n
    Inherits:
        cmd.Cmd (class)
    """
    prompt = "(hbnb) "
    valid_classes = ["BaseModel", "User", "State", "City",
                  "Amenity", "Place", "Review"]

    def do_quit(self, line):
        """Function that exits the program
        """
        return True

    def do_EOF(self, line):
        """Function that exits the program
        """
        return True

    def emptyline(self):
        """Executes when no commands input
        """
        return False
    @staticmethod
    def get_args(argstr : str) -> dict:
        """Utility function to tokenize a string of arguments to
        individual arguments\n
        Args:
            `args` (str) - arg string
        Returns:
            `args` (dict) - dictionary of arguments\n
            (class_name, id, attr, val)
        """
        args = argstr.split(" ")
        cls_name = args[0] if len(args) > 0 else None
        id = args[1] if len(args) > 1 else "no_id"
        attr = args[2] if len(args) > 2 else "not_upd"
        val = args[3].strip(' "' + "'") if len(args) > 3 else "not_upd"

        return {'cls_name': cls_name, 'id': id,'attr': attr,
                'val': val}

    @staticmethod
    def is_valid_class(args) -> bool:
        """(Utility function) -> Checks if class name is valid\n
        Args:
            `args` (str) - argument string\n
        Returns:
            `True` | `False` if class name is valid or not
        """
        (cls_name, id, attr, val) = HBNBCommand.get_args(args).values()
        obj = HBNBCommand.get_obj(cls_name, id)

        if not cls_name:
            print("** class name missing **")
            return False
        elif cls_name not in HBNBCommand.valid_classes:
            print("** class doesn't exist **")
            return False
        elif not id:
            print("** instance id missing **")
            return False
        elif id != "no_id" and not obj:
            # if id exists and is wrong
            print("** no instance found **")
            return False
        elif attr != "not_upd" and not attr:
            print("** attribute name missing **")
            return False
        elif val != "not_upd" and not val:
            print("** value missing **")
            return False
        else:
            return True

    @staticmethod
    def get_obj(cls_name, id):
        """Function that gets instance given the id\n
        Args:
            `cls_name` (str) - class name\n
            `id` (str) - the id of instance\n
        Returns:
            `object` - instance
        """
        objs = storage.all()
        for value in list(objs.values()):
            obj_dict = value.to_dict()
            inst_id = obj_dict["id"]
            inst_name = obj_dict["__class__"]
            if inst_id == id and inst_name == cls_name:
                return (value)

        return None

    def do_create(self, args):
        """Usage: `create <class name>`\n
        Function that creates new instance of BaseModel,
        saves it to JSON file and prints the id\n
        Args:
            `args` (str) - string of commands to execute
        """
        if self.is_valid_class(args):
            cls_name = HBNBCommand.get_args(args)['cls_name']
            new = eval(cls_name)()
            new.save()
            print(new.id)


    def do_show(self, args : str):
        """Usage: `show <class name> <id>`\n
        Function that prints the string representation of
        object based on object name and id\n
            `args` (str) - string of commands to execute
        """
        if self.is_valid_class(args):
            obj = HBNBCommand.get_args(args)['obj']
            print(obj)

    def do_destroy(self, args):
        """Usage: `destroy <class name> <id>`\n
        Function that deletes an instance based on the class name
        and id (save the change into the JSON file)\n
        Args:
            `args` (str) - string of commands to execute\n
        """
        if self.is_valid_class(args):
            (cls_name, id, _, _) = HBNBCommand.get_args(args).values()
            obj = HBNBCommand.get_obj(cls_name, id)
            key = obj.to_dict()['__class__'] + "." + obj.id
            del storage.all()[key]
            storage.save()

    def do_all(self, args):
        """Usage: `all <class name>` or `all`\n
        Prints all string representation of all instances based
        or not on the class name\n
        Args:
            `args` (str) - string of commands to execute\n
        """
        all_objs = storage.all()
        obj_list = []
        cls_name = HBNBCommand.get_args(args)['cls_name']
        if not cls_name:
            obj_list = list("{}".format(value)
                            for value in list(all_objs.values()))
            print(obj_list)
        elif self.is_valid_class(args):
            obj_list = list("{}".format(value)
                            for value in list(all_objs.values())
                            if value.to_dict()['__class__']
                            == cls_name)
            print(obj_list)

    def do_update(self, args):
        """Usage: update `<class name>` `<id>` `<attribute name> `
        `"<attribute value>"`\n
        Function that updates an instance based on the class name
        and id by adding or updating attribute
        (save the change into the JSON file)\n
        Args:
            `args` (str) - string of commands to execute\n
        """
        (cls_name, id, attr, val) = HBNBCommand.get_args(args).values()
        obj = HBNBCommand.get_obj(cls_name, id)

        if self.is_valid_class(args):
            if obj.to_dict().get(attr):
                obj_dict = obj.__dict__
                ty_pe = type(obj_dict[attr])
                obj_dict[attr] = ty_pe(val)
            elif not obj.to_dict().get(attr):
                obj_key = obj.to_dict()['__class__'] + "." + obj.id
                setattr(storage.all()[obj_key], attr, val)
            elif type(obj) == str:
                print(obj)
            storage.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
