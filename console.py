#!/usr/bin/python3
"""this module contains the entry point of the command interpreter"""

import json
import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """Simple command processor that manages the AirBnB objects"""
    prompt = '(hbnb) '
    hn_class = ['BaseModel']

    def do_create(self, cl_name):
        """command that creates a new instance of BaseModel\
                saves it to the JSON file, and prints the id
        """
        if not cl_name:
            print("** class name missing **")
        if cl_name != 'BaseModel':
            print("** class doesn't exist **")

        new_instance = BaseModel()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, args):
        """Prints the string representation of an instance based on the\
                class name and id
        """
        arg = args.split(' ')
        if not arg[0]:
            print("** class name missing **")
        elif arg[0] != 'BaseModel':
            print("** class doesn't exist **")
        elif len(arg) != 2:
            print("** instance id is missing **")
        else:
            obj = storage.all()
            for k, v in obj.items():
                obj_name = v.__class__.__name__

                if obj_name == arg[0] and arg[1].strip('"') == v.id:
                    print(v)
                    return
            print("** no instance found **")

    def do_destroy(self, args):
        """Deletes an instance based on the class name and id"""
        arg = args.split(' ')
        if not arg[0]:
            print("** class name missing **")
        elif arg[0] != 'BaseModel':
            print("** class doesn't exist **")
        elif len(arg) != 2:
            print("** instance id is missing **")
        else:
            obj = storage.all()
            for k, v in obj.items():
                obj_name = v.__class__.__name__
                if obj_name == arg[0] and arg[1].strip('"') == v.id:
                    del obj[k]
                    storage.save()
                    return
            print("** no instance found **")

    def do_all(self, cl_name):
        """Prints all string representation of all instances\
                based on or not on the class name
        """
        if cl_name.split() != 'BaseModel':
            print("** class doesn't exist **")

        new_list = []
        obj = storage.all()
        for k, v in obj.items():
            obj_name = v.__class__.__name__
            if cl_name == obj_name:
                new_list.append(str(v))
        print(json.dumps(new_list))

    def do_update(self, args):
        """Updates an instance based on the class name and id by\
                adding or updating attribute (save the change into\
                the JSON file)
        """
        arg = args.split()
        if not arg[0]:
            print("** class name missing **")
        elif arg[0] != 'BaseModel':
            print("** class doesn't exist **")
        elif len(arg) == 1:
            print("** instance id missing **")
        elif len(arg) == 2:
            print("** attribute name missing **")
        elif len(arg) == 3:
            print("** value missing **")
        else:
            obj = storage.all()
            for k, v in obj.items():
                obj_name = v.__class__.__name__
                if arg[0] == obj_name and arg[1].strip('"') == v.id:
                    setattr(v, arg[2], arg[3])
                    storage.save()
                return
            print("** no instance found **")

    def emptyline(self):
        """makes sure that an emptyline or ENTER doesn't execute anything"""
        pass

    def do_EOF(self, line):
        """EOF command to exit the progam"""
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
