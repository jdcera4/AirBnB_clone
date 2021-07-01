#!/usr/bin/python3
""" console """
import cmd
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models import storage
from models.user import User
import parser


class HBNBCommand(cmd.Cmd):
    ''' Console '''
    prompt = "(hbnb) "
    __models_list = ['Amenity', 'BaseModel',
                     'City', 'Place', 'Review', 'State', 'User']
    __prev_objects = storage.all()

    def emptyline(self):
        """ empty line
        """
        pass

    def do_EOF(self, line):
        ''' Exit the console
        '''
        print()
        return True

    def do_quit(self, line):
        ''' Quit the console
        '''
        return True

    def do_create(self, args):
        ''' Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id.
        Ex: $ create BaseModel
        '''
        arg = args.split(" ")
        if not args:
            print('** class name missing **')
        elif arg[0] not in self.__models_list:
            print('''** class doesn't exist **''')
        else:
            # create basemodel
            new_obj = eval("{}()".format(arg[0]))
            new_obj.save()
            # print the ID
            print(new_obj.id)

    def do_show(self, arg):
        '''Prints the string representation of an instance
        based on the class name and id.
        '''
        if not arg:
            print('** class name missing **')
        else:
            arg = arg.split()
            if arg[0] not in self.__models_list:
                print('''** class doesn't exist **''')
            elif len(arg) == 1:
                print('** instance id missing **')
            else:
                obj_name = "{}.{}".format(arg[0], arg[1])
                if obj_name in self.__prev_objects.keys():
                    print(self.__prev_objects[obj_name])
                else:
                    print('** no instance found **')

    def do_destroy(self, arg):
        '''Deletes an instance based on the class name
        and id (save the change into the JSON file)
        Ex: $ destroy BaseModel 1234-1234-1234.
        '''
        if not arg:
            print('** class name missing **')
        else:
            arg = arg.split()
            if arg[0] not in self.__models_list:
                print('''** class doesn't exist **''')
            elif len(arg) == 1:
                print('** instance id missing **')
            else:
                obj_name = "{}.{}".format(arg[0], arg[1])
                if obj_name in self.__prev_objects.keys():
                    self.__prev_objects.pop(obj_name)
                    storage.save()
                else:
                    print('** no instance found **')

    def do_all(self, line):
        """Prints all string representation of all instances
        Exceptions:
            NameError: when there is no object taht has the name
        """
        objects = storage.all()
        my_list = []
        if not line:
            print('** class name missing **')
        try:
            args = line.split(" ")
            if args[0] not in self.__models_list:
                raise NameError()
            for key in objects:
                name = key.split('.')
                if name[0] == args[0]:
                    my_list.append(objects[key])
            print(my_list)
        except NameError:
            print("** class doesn't exist **")

    def do_update(self, args):
        '''Updates an instance based on the class name and id
        by adding or updating attribute (save the change into
        the JSON file). Ex: $ update BaseModel 1234-1234-1234
        email "aibnb@holbertonschool.com".
        '''
        if not args:
            print("** class name missing **")
        else:
            my_list = args.split()
            if my_list[0] not in self.__models_list:
                print("** class doesn't exist **")
            elif len(my_list) == 1:
                print("** instance id missing **")
            else:
                key = my_list[0] + '.' + my_list[1]
                if key not in self.__prev_objects.keys():
                    print("** no instance found **")
                elif len(my_list) < 3:
                    print("** attribute name missing **")
                elif len(my_list) < 4:
                    print("** value missing **")
                else:
                    self.__prev_objects[key].\
                        __dict__[my_list[2]] = eval(my_list[3])
                    storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
