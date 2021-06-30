#!/usr/bin/python3
"""Unittest for AirBnB - Console / amenity
"""
import os
import unittest
import models.amenity
from models.amenity import Amenity
from models.base_model import BaseModel


class Test_Base_Reqeriments(unittest.TestCase):
    """Class to test the amenity class requeriments"""

    # Testing pep8 and shebang
    def test_pep8_Base(os_system):
        """PEP8 validation"""
        os_system.assertEqual(os.system("pep8 ./models/amenity.py"), 0)

    def test_pep8_test_base(os_system):
        """PEP8 validation"""
        path = os.system("pep8 tests/test_models/test_amenity.py")
        os_system.assertEqual(path, 0)

    def test_shebang(self):
        """First line contains #!/usr/bin/python3"""
        with open('./models/amenity.py', 'r') as fd:
            x = fd.read()
            line = x.splitlines()
            self.assertEqual(line[0], '#!/usr/bin/python3')

    def test_shebang_test_base(self):
        """First line contains #!/usr/bin/python3"""
        with open('./tests/test_models/test_amenity.py', 'r') as fd:
            x = fd.read()
            line = x.splitlines()
            self.assertEqual(line[0], '#!/usr/bin/python3')

    # Documentation for Module, class and methods exist
    def test_docmodule(self):
        """Module is documented"""
        temp = models.amenity.__doc__
        self.assertTrue(temp is not None and len(temp) > 0)

    def test_docclass(self):
        """Class is documented"""
        temp = Amenity.__doc__
        self.assertTrue(temp is not None and len(temp) > 0)


class Test_Amenity(unittest.TestCase):
    '''Class to test the Amenity class Attributes'''
    @classmethod
    def setUpClass(cls):
        '''Create instance to test the attributes of a class'''
        cls.amenity = Amenity()

    @classmethod
    def tearDownClass(cls):
        '''Remove the istance after run tests'''
        del cls.amenity

    def test_inheritance_from_BaseModel(self):
        '''test if User class is a subclas of BaseModel'''
        self.assertTrue(issubclass(type(self.amenity), BaseModel))

    def test_attributes(self):
        '''test if de Amenity class have the attributte and if is str'''
        # Email
        self.assertTrue(hasattr(self.amenity, "name"))    # Att exists
        self.assertIsInstance(self.amenity.name, str)     # Att is string
        self.assertTrue(self.amenity.name == "")          # Att is empty
