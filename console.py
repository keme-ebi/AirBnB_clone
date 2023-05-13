#!/usr/bin/python3
"""this module contains the entry point of the command interpreter"""

import cmd


class HBNBCommand(cmd.Cmd):
    """Simple command processor that manages the AirBnB objects"""
    prompt = '(hbnb)'

    def emptyline(self):
        """makes sure that an emptyline or ENTER doesn't execute anything"""

    def do_EOF(self, line):
        """EOF command to exit the progam"""
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
