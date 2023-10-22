#!/usr/bin/python3
""" Defines the HBnB console. """

import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.review import Review
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models import storage
import re


class HBNBCommand(cmd.Cmd):
    """The entry point of the command interpreter"""

    prompt = '(hbnb) '
    __classes = {
            "BaseModel",
            "User",
            "State",
            "City",
            "Review",
            "Amenity",
            "Place"
            }

    def emptyline(self):
        """ Do nothing upon empty line and enter"""
        pass

    def default(self, arg):
        tmp = arg.split('.')
        if len(tmp) == 1 or tmp[1] == '' or tmp[0] not in self.__classes:
            print("*** Unknown syntax: {}".format(arg))
            return
        else:
            mtd_name = re.match(r'^\w+', tmp[1]).group()
            cnt = re.findall(r'\((.*?)\)', tmp[1])
            if len(tmp) == 2:
                if tmp[1] == "all()":
                    self.do_all(tmp[0])
                elif tmp[1] == "count()":
                    i = 0
                    for k, v in storage.all().items():
                        if v.__class__.__name__ == tmp[0]:
                            i += 1
                    print(i)
                elif mtd_name == "show":
                    if len(cnt) > 0:
                        arg_ = "{} {}".format(tmp[0], cnt[0].strip("'\""))
                        self.do_show(arg_)
                elif mtd_name == "destroy":
                    if len(cnt) > 0:
                        arg_ = "{} {}".format(tmp[0], cnt[0].strip("'\""))
                        self.do_destroy(arg_)

            else:
                 print("*** Unknown syntax: {}".format(arg))

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
            print("** class name missing **")
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
            print("** class name missing **")
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
    def do_update(self, arg):

        """
        Update an instance based on the class name and id 

        """
        no_update = {
                "id",
                "created_at",
                "updated_at"
                }
        args = [s.strip('\'"') for s in re.findall(r'\'[^\']*\'|"[^"]*"|\S+', arg)]
        if len(args) == 0:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in self.__classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        obj_id = args[1]
        key = "{}.{}".format(class_name, obj_id)
        if key not in storage.all():
            print("** no instance found **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return

        attr_name = args[2]
        if attr_name in no_update:
            if len(args) > 3:
                print("** attribute can't be updated **")
                return
        if len(args) < 4:
            print("** value missing **")
            return

        attr_value = args[3].strip()
        data = storage.all()
        to_update = data['{}.{}'.format(args[0], args[1])]
        setattr(to_update, attr_name, attr_value)
        to_update.save()



if __name__ == '__main__':
    HBNBCommand().cmdloop()
