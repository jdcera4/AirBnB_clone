#!/usr/bin/python3
import cmd
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models import storage
from models.user import User


class HBNBCommand(cmd.Cmd):
    ''' Console '''
    prompt = "(hbnb) "
    models_list = ['Amenity', 'BaseModel', 'City',
    'Place', 'Review', 'State', 'User']
    prev_objects = storage.all()

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

    def do_create(self, args):
        ''' Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id.
        Ex: $ create BaseModel'''
        if not args:
            print('** class name missing **')
        elif args not in self.models_list:
            print('''** class doesn't exist **''')
        else:
            # create basemodel
            # print the ID
            pass

    def to_show(self, arg):
        '''Prints the string representation of an instance
        based on the class name and id.'''
        if not arg:
            print('** class name missing **')
        else:
            arg = arg.split()
            if arg[0] not in self.models_list:
                print('''** class doesn't exist **''')
            elif not arg[1]:
                print('** instance id missing **')
            else:
                obj_name = "{}.{}".format(arg[0], arg[1])
                if obj_name not in self.prev_objects.keys():
                    # print string representation
                    pass
                else:
                    print('** no instance found **')

    def to_destroy(self, arg):
        '''Deletes an instance based on the class name
        and id (save the change into the JSON file)
        Ex: $ destroy BaseModel 1234-1234-1234.'''
        pass

    def to_all(self, arg):
        '''Prints all string representation of all instances
        based or not on the class name. Ex: $ all BaseModel or $ all.'''
        pass

    def to_update(self, arg):
        '''Updates an instance based on the class name and id
        by adding or updating attribute (save the change into
        the JSON file). Ex: $ update BaseModel 1234-1234-1234
        email "aibnb@holbertonschool.com".'''
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
