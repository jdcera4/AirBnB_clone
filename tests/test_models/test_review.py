#!/usr/bin/python3
"""Unittest for AirBnB - Console / review
"""
import os
import unittest
import models.review
from models.review import Review
from models.base_model import BaseModel


class Test_review_Reqeriments(unittest.TestCase):
    """Class to test the review class requeriments"""

    # Testing pep8 and shebang
    def test_pep8_Base(os_system):
        """PEP8 validation"""
        os_system.assertEqual(os.system("pep8 ./models/review.py"), 0)

    def test_pep8_test_base(os_system):
        """PEP8 validation"""
        path = os.system("pep8 tests/test_models/test_review.py")
        os_system.assertEqual(path, 0)

    def test_shebang(self):
        """First line contains #!/usr/bin/python3"""
        with open('./models/review.py', 'r') as fd:
            x = fd.read()
            line = x.splitlines()
            self.assertEqual(line[0], '#!/usr/bin/python3')

    def test_shebang_test_base(self):
        """First line contains #!/usr/bin/python3"""
        with open('./tests/test_models/test_review.py', 'r') as fd:
            x = fd.read()
            line = x.splitlines()
            self.assertEqual(line[0], '#!/usr/bin/python3')

    # Documentation for Module, class and methods exist
    def test_docmodule(self):
        """Module is documented"""
        temp = models.review.__doc__
        self.assertTrue(temp is not None and len(temp) > 0)

    def test_docclass(self):
        """Class is documented"""
        temp = Review.__doc__
        self.assertTrue(temp is not None and len(temp) > 0)


class Test_Review(unittest.TestCase):
    '''Class to test the Review class Attributes'''
    @classmethod
    def setUpClass(cls):
        '''Create instance to test the attributes of a class'''
        cls.review = Review()

    @classmethod
    def tearDownClass(cls):
        '''Remove the istance after run tests'''
        del cls.review

    def test_inheritance_from_BaseModel(self):
        '''test if review class is a subclas of BaseModel'''
        self.assertTrue(issubclass(type(self.review), BaseModel))

    def test_attributes(self):
        '''test if de place class have the attributte and if is str'''
        # place_id
        self.assertTrue(hasattr(self.review, "place_id"))    # Att exists
        self.assertIsInstance(self.review.place_id, str)     # Att is string
        self.assertTrue(self.review.place_id == "")
        # user_id
        self.assertTrue(hasattr(self.review, "user_id"))
        self.assertIsInstance(self.review.user_id, str)
        self.assertTrue(self.review.user_id == "")
        # text
        self.assertTrue(hasattr(self.review, "text"))
        self.assertIsInstance(self.review.text, str)
        self.assertTrue(self.review.text == "")
