import cmd


class HBNBCommand(cmd.Cmd):
    """The entry point of the command interpreter"""

    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit on EOF"""
        print("")
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
