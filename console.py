#!/usr/bin/python3
""" Defines the HBnB console. """

import cmd
from models.base_model import BaseModel
from models.user import User
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
                    new_class.save()
                    break;
            else:
                print ("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_show(self, arg):
        """ Prints the string representation of an instance """

        if arg:
            _arg = arg.split()
            if len(_arg) < 2:
                print('** instance id missing **')
            else:
                for clss in self.__classes:
                    if clss == _arg[0]:
                        _all = storage.all()
                        _pnt = "{}.{}".format(_arg[0], _arg[1])
                        try:
                            print(_all[_pnt])
                        except KeyError:
                            print("** no instance found **")
                        break;
                else:
                    print("** class doesn't exist **")
        else:
            print("** class name missing ***")
    def do_destroy(self, arg):
        """ Deletes an instance based on the class name and id """

        if arg:
            _arg = arg.split()
            if len(_arg) < 2:
                print('** instance id missing **')
            else:
                for clss in self.__classes:
                    if clss == _arg[0]:
                        _all = storage.all()
                        _pnt = "{}.{}".format(_arg[0], _arg[1])
                        try:
                            del _all[_pnt]
                            storage.save()
                        except KeyError:
                            print("** no instance found **")
                        break;
                else:
                    print("** class doesn't exist **")
        else:
            print("** class name missing ***")
    def do_all(self, arg):
        """ Prints all string representation of all instacnes based """
        t_all = storage.all()
        array_t_0 = []
        if arg:
            condition_ = False
            tmp_arg = arg.split()
            for clss in  self.__classes:
                if clss == tmp_arg[0]:
                    for key, value in t_all.items():
                        if value.__class__.__name__ == tmp_arg[0]:
                            condition_ = True
                            array_t_0.append(value.__str__())
                            print(array_t_0)
            if not condition_:
                print ("** class doesn't exist **")
        else:
            for k, v in t_all.items():
                array_t_0.append(v.__str__())
            print(array_t_0)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
