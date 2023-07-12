#!/usr/bin/python3
"""
This is the entry point for the command interpreter
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """
    Runs a command line interpreter for our program
    """

    prompt = '(hbnb) '

    def do_quit(self, line):
        """ Quit command to exit the program """
        return (True)

    def do_EOF(self, line):
        """ EOF command to exit the program """
        return (True)

    def emptyline(self):
        """ an empty line + ENTER key does nothing """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
