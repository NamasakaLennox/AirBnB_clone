#!/usr/bin/python3
"""
A module that contains the console
"""
from models.base_model import BaseModel
import cmd
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    A cmd interpretor class

    Inherits:
        cmd.Cmd (class)
    """
    prompt = "(hbnb)"

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
    def is_valid_class(args):
        """Checks if class name is valid

        Args:(args)
            `cls_name` (str) - class name\n
            `id` (str) - uuid of class\n
        Returns:
            `True` | `False` if class name is valid or not
        """
        cmds = args.split(" ")
        cls_name = cmds[0] if len(cmds) > 0 else None
        id = cmds[1] if len(cmds) > 1 else None

        if not cls_name:
            print("** class name missing **")
            return False
        elif cls_name not in ['BaseModel']:
            print("** class doesn't exist **")
            return False
        elif not id:
            print("** instance id missing **")
            return False
        else:
            return True

    @staticmethod
    def get_obj(id):
        """Function that gets instance given the id

        Args:
            id (str) - the id of instance
        Returns:
            object | str (if no instance is found)
        """
        objs = storage.all()
        if len(list(objs.values())) < 1:
            return ("** no instance found **")
        for value in list(objs.values()):
            obj_dict = value.to_dict()
            if obj_dict["id"] == id:
                return (value)
        else:
            return ("** no instance found **")

    def do_create(self, args):
        """Function that creates new instance of BaseModel,
        saves it to JSON file and prints the id
        """
        args_ls = args.split(" ")
        cls_name = args_ls[0] if len(args_ls) > 0 else ""
        if self.is_valid_class(cls_name + " no_id"):
            new = BaseModel() if cls_name == 'BaseModel' else BaseModel()
            print(new.id)

    def do_show(self, args : str):
        """Function that prints the string representation of
        object based on object name and id
        """
        if self.is_valid_class(args):
            args_ls = args.split(" ")
            id = args_ls[1] if len(args_ls) > 1 else "no_id"
            obj = self.get_obj(id)
            print(obj)

    def do_destroy(self, args):
        """Function that deletes an instance based on the class name
        and id (save the change into the JSON file)

        Args:
            cls_name (str) - class name
            id (str) - uuid of class
        """
        if self.is_valid_class(args):
            args_ls = args.split(" ")
            id = args_ls[1] if len(args_ls) > 1 else ""
            obj = self.get_obj(id)

            if type(obj) == str:
                print(obj)
            elif  obj and type(obj) != str:
                key = obj.to_dict()['__class__'] + "." + obj.id
                del storage.all()[key]

    def do_all(self, args):
        """ Prints all string representation of all instances based
        or not on the class name\n
        Args:
            `*args` (str) - class name\n
        """
        args_ls = args.split(" ")
        all_objs = storage.all()
        obj_list = []
        cls_name = args_ls[0] if len(args_ls) > 0 else ""

        if not cls_name:
            obj_list = list("{}".format(value)
                            for value in list(all_objs.values()))
            print(obj_list)
        elif self.is_valid_class(cls_name + " no_id"):
            obj_list = list("{}".format(value)
                            for value in list(all_objs.values())
                            if value.to_dict()['__class__']
                            == cls_name)
            print(obj_list)

    def do_update(self, args):
        """Usage: update `<class name>` `<id>` `<attribute name>` `"<attribute value>"`\n
        Function that updates an instance based on the class name
        and id by adding or updating attribute
        (save the change into the JSON file)

        Args: (args)
            `class name`  - class name,\n
            `id`  - id of class,\n
            `attr`  - attribute to change,\n
            `val`  - new value of attr\n
        """
        cmds = args.split(" ")
        attr = cmds[2] if len(cmds) > 2 else None
        exp = ""
        val = cmds[3].strip(' "' + "'") if len(cmds) > 3 else None
        if not attr:
            print("** attribute name missing **")
        elif not val:
            print("** value missing **")
        elif self.is_valid_class(args):
            obj = self.get_obj(cmds[1])

            if type(obj) != str and obj.to_dict().get(attr):
                ty_pe = type(obj.to_dict()[attr])
                setattr(obj, attr, ty_pe(val))
            elif type(obj) == str:
                print(obj)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
