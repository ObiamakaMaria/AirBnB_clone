#!/usr/bin/python3
""" Defines the HBnB console. """

import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """The entry point of the command interpreter"""

    prompt = '(hbnb) '
    __classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
    }

    def emptyline(self):
        """ Do nothing upon empty line and enter"""
        pass
     
    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit on EOF"""
        print("")
        return True
    
    def do_create(self, arg):
        """ Creates a new instance of BaseModel """

        if arg:
            tmp_arg = arg.split()
            for clss in  self.__classes:
                if clss == tmp_arg[0]:
                   new_class = eval('{}()'.format(tmp_arg[0]))
                   print(new_class.id)
                   storage.save()
                   break;
            else:
                print ("** class doesn't exist **")
        else:
            print("** class name missing **")
    
    def do_show(self, arg):
        """ Prints the string representation of an instance """
        
        tmp_arg = arg.split()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
