#!/usr/bin/python3
"""Unittest for AirBnB - Console / city
"""
import os
import unittest
import models.city
from models.city import City
from models.base_model import BaseModel


class Test_Base_Reqeriments(unittest.TestCase):
    """Class to test the city class requeriments"""

    # Testing pep8 and shebang
    def test_pep8_Base(os_system):
        """PEP8 validation"""
        os_system.assertEqual(os.system("pep8 ./models/city.py"), 0)

    def test_pep8_test_base(os_system):
        """PEP8 validation"""
        path = os.system("pep8 tests/test_models/test_city.py")
        os_system.assertEqual(path, 0)

    def test_shebang(self):
        """First line contains #!/usr/bin/python3"""
        with open('./models/city.py', 'r') as fd:
            x = fd.read()
            line = x.splitlines()
            self.assertEqual(line[0], '#!/usr/bin/python3')

    def test_shebang_test_base(self):
        """First line contains #!/usr/bin/python3"""
        with open('./tests/test_models/test_city.py', 'r') as fd:
            x = fd.read()
            line = x.splitlines()
            self.assertEqual(line[0], '#!/usr/bin/python3')

    # Documentation for Module, class and methods exist
    def test_docmodule(self):
        """Module is documented"""
        temp = models.city.__doc__
        self.assertTrue(temp is not None and len(temp) > 0)

    def test_docclass(self):
        """Class is documented"""
        temp = City.__doc__
        self.assertTrue(temp is not None and len(temp) > 0)


class Test_Amenity(unittest.TestCase):
    '''Class to test the Amenity class Attributes'''
    @classmethod
    def setUpClass(cls):
        '''Create instance to test the attributes of a class'''
        cls.city = City()

    @classmethod
    def tearDownClass(cls):
        '''Remove the istance after run tests'''
        del cls.city

    def test_inheritance_from_BaseModel(self):
        '''test if User class is a subclas of BaseModel'''
        self.assertTrue(issubclass(type(self.city), BaseModel))

    def test_attributes(self):
        '''test if de City class have the attributte and if is str'''
        # name
        self.assertTrue(hasattr(self.city, "name"))    # Att exists
        self.assertIsInstance(self.city.name, str)     # Att is string
        self.assertTrue(self.city.name == "")          # Att is empty
        # state_id
        self.assertTrue(hasattr(self.city, "state_id"))    # Att exists
        self.assertIsInstance(self.city.state_id, str)     # Att is string
        self.assertTrue(self.city.state_id == "")          # Att is empty