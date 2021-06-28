#!/usr/bin/python3
'''
Unittest for AirBnB - Console / base
'''
import os
import uuid
import unittest
import models.base_model
from models.base_model import BaseModel
from datetime import datetime


class Test_Base_Reqeriments(unittest.TestCase):
    '''Class to test the base_model class requeriments'''

    # Testing pep8 and shebang
    def test_pep8_Base(os_system):
        '''PEP8 validation'''
        os_system.assertEqual(os.system("pep8 ./models/base_model.py"), 0)

    def test_pep8_test_base(os_system):
        '''PEP8 validation'''
        path = os.system("pep8 tests/test_models/test_base_model.py")
        os_system.assertEqual(path, 0)

    def test_shebang(self):
        '''First line contains #!/usr/bin/python3'''
        with open('./models/base_model.py', 'r') as fd:
            x = fd.read()
            line = x.splitlines()
            self.assertEqual(line[0], '#!/usr/bin/python3')

    def test_shebang_test_base(self):
        '''First line contains #!/usr/bin/python3'''
        with open('./tests/test_models/test_base_model.py', 'r') as fd:
            x = fd.read()
            line = x.splitlines()
            self.assertEqual(line[0], '#!/usr/bin/python3')

    # Documentation for Module, class and methods exist
    def test_docmodule(self):
        '''Module is documented'''
        self.assertIsNotNone(models.base_model.__doc__)

    def test_docclass(self):
        '''Class is documented'''
        self.assertIsNotNone(BaseModel.__doc__)

    def test_constructor(self):
        '''init is documented'''
        self.assertIsNotNone(BaseModel.__init__.__doc__)

    def test_doc_methods(self):
        '''Functions are documented'''
        # save
        self.assertIsNotNone(BaseModel.save.__doc__)
        # to_dict
        self.assertIsNotNone(BaseModel.to_dict.__doc__)
        # Str
        self.assertIsNotNone(BaseModel.__str__.__doc__)


class Test_BaseModel(unittest.TestCase):
    '''Class to test the BaseModel class Attributes & Methods'''
    @classmethod
    def setUpClass(cls):
        '''Create instance to test the attributes of a class'''
        cls.baseA = BaseModel()
        cls.baseB = BaseModel()

    @classmethod
    def tearDownClass(cls):
        '''Remove the istance after run tests'''
        del cls.base

    def test_inheritance_from_BaseModel(self):
        '''test if User class is a subclas of BaseModel'''
        self.assertTrue(issubclass(type(self.base), object))

    def test_instance_attributes(self):
        # id
        self.assertTrue(hasattr(self.baseA, "id"))    # Att exists
        self.assertIsInstance(self.baseA.id, uuid.UUID)     # Att is string
        self.assertNotEqual(self.baseA.id, self.baseB.id)
        # created_at
        self.assertTrue(hasattr(self.baseA, "created_at"))
        self.assertIsInstance(self.baseA.created_at, datetime)
        # updated_at
        self.assertTrue(hasattr(self.baseA, "updated_at"))
        self.assertIsInstance(self.baseA.updated_at, datetime)

    def test_str(self):
        self.assertTrue(type(self.baseA.__str__) == str)

    def test_save(self):
        update1 = self.baseA.updated_at
        create1 = self.baseA.created_at
        self.baseA.save()
        update2 = self.baseA.updated_at
        create2 = self.baseA.created_at
        self.assertNotEqual(update1, update2)
        self.assertEqual(create1, create2)

    def test_to_dict(self):
        x = self.baseA.to_dict()
        self.assertTrue(type(x["create_at"] == str))