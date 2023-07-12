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
    def is_valid_class(cls_name, id="1234"):
        """Checks if class name is valid

        Args:
            cls_name (str) - class name
            id (str) - uuid of class
        Returns:
            True | False if class name is valid or not
        """
        if len(cls_name) < 1:
            print("** class name missing **")
            return False
        elif cls_name not in ['BaseModel']:
            print("** class doesn't exist **")
            return False
        elif not id or len(id) < 1:
            print("** instance id missing **")
            return False
        else:
            return True

    @staticmethod
    def get_obj(id):
        """Function that gets `dict` representation of instance id

        Args:
            id (str) - the id of instance
        Returns:
            dict | str if no instance is found
        """
        objs = storage.all()
        return (objs.get(id) if objs.get(id)
                else "** no instance found **")

    def do_create(self, cls_name):
        """Function that creates new instance of BaseModel,
        saves it to JSON file and prints the id
        """
        if self.is_valid_class(cls_name):
            new = BaseModel()
            print(new.id)

    def do_show(self, cls_name, id=None):
        """Function that prints the string representation of
        object based on object name and id
        """
        if self.is_valid_class(cls_name, id):
            obj = self.get_obj(id)
            if type(obj) == dict:
                new_inst = BaseModel(**obj)
                print(new_inst)

    def do_destroy(self, cls_name, id):
        """Function that deletes an instance based on the class name
        and id (save the change into the JSON file)

        Args:
            cls_name (str) - class name
            id (str) - uuid of class
        """
        if self.is_valid_class(cls_name, id):
            obj = self.get_obj(id)
            if type(obj) == dict:
                del obj
            else:
                print(obj)

    def do_all(self, cls_name):
        """ Prints all string representation of all instances based
        or not on the class name
        Args:
            cls_name (str) - class name
        """
        all_objs = storage.all()
        obj_list = []

        if len(cls_name) < 1:
            obj_list = list("{}".format(BaseModel(**value))
                            for value in list(all_objs.values()))
            print(obj_list)
        elif self.is_valid_class(cls_name):
            obj_list = list("{}".format(BaseModel(**value))
                            for value in list(all_objs.values())
                            if value['__class__'] == cls_name)
            print(obj_list)

    def do_update(self, cls_name, id, attr, val):
        """Function that updates an instance based on the class name
        and id by adding or updating attribute
        (save the change into the JSON file)

        Args:
            `cls_name` - class name,
            `id` - id of class,
            `attr` - attribute to change,
            `val` - new value of attr
        """

        if len(attr) < 1:
            print("** attribute name missing **")
        elif len(val) < 1:
            print("** value missing **")
        elif self.is_valid_class(cls_name, id):
            obj = self.get_obj(id)
            if type(obj) == dict and obj.get(attr):
                ty_pe = type(obj[attr])
                obj[attr] = ty_pe(val)
            elif type(obj) != dict:
                print(obj)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
