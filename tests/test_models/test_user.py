#!/usr/bin/python3
'''Unittest for AirBnB - Console / user
'''
import os
import unittest
import models.user
from models.user import User


class Test_Base_Reqeriments(unittest.TestCase):
    '''Class to test the user class requeriments'''

    # Testing pep8 and shebang
    def test_pep8_Base(os_system):
        '''PEP8 validation'''
        os_system.assertEqual(os.system("pep8 ./models/user.py"), 0)

    def test_pep8_test_base(os_system):
        '''PEP8 validation'''
        path = os.system("pep8 tests/test_models/test_user.py")
        os_system.assertEqual(path, 0)

    def test_shebang(self):
        '''First line contains #!/usr/bin/python3'''
        with open('./models/user.py', 'r') as fd:
            x = fd.read()
            line = x.splitlines()
            self.assertEqual(line[0], '#!/usr/bin/python3')

    def test_shebang_test_base(self):
        '''First line contains #!/usr/bin/python3'''
        with open('./tests/test_models/test_user.py', 'r') as fd:
            x = fd.read()
            line = x.splitlines()
            self.assertEqual(line[0], '#!/usr/bin/python3')

    # Documentation for Module, class and methods exist
    def test_docmodule(self):
        '''Module is documented'''
        # temp = models.user.__doc__
        # self.assertTrue(temp is not None and len(temp) > 0)
        self.assertIsNotNone(models.user.__doc__)

    def test_docclass(self):
        '''Class is documented'''
        # temp = User.__doc__
        # self.assertTrue(temp is not None and len(temp) > 0)
        self.assertIsNotNone(User.__doc__)


class Test_User(unittest.TestCase):
    '''Class to test the User class Attributes'''
    def test_inheritance_from_BaseModel(self):
        '''test if User class is a subclas of BaseModel'''
        self.assertTrue(issubclass(type(self.user), BaseModel))

    def test_attributes(self):
        '''test if de User class have the attributte and if is str'''
        # Email
        self.assertTrue(hasattr(self.user, "email")) # Att exists
        self.assertIsInstance(self.user.email, str)  # Att is string
        self.assertTrue(self.user.email == "")       # Att is empty
        # Password
        self.assertTrue(hasattr(self.user, "password"))
        self.assertIsInstance(self.user.password, str)
        self.assertTrue(self.user.password == "")
        # First Name
        self.assertTrue(hasattr(self.user, "first_name"))
        self.assertIsInstance(self.user.first_name, str)
        self.assertTrue(self.user.first_name == "")
        # Last Name
        self.assertTrue(hasattr(self.user, "last_name"))
        self.assertIsInstance(self.user.last_name, str)
        self.assertTrue(self.user.last_name == "")
