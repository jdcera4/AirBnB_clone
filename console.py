#!/usr/bin/python3
import cmd


class HBNBCommand(cmd.Cmd):
    ''' Console '''
    prompt = "(hbnb) "
 
    def do_EOF(self, line):
        ''' Exit the console '''
        print()
        return True

    def do_quit(self, line):
        ''' Quit the console '''
        return True

    def emptyline(self):
        ''' Do nothing on empty line '''
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
