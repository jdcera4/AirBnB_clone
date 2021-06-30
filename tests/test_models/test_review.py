#!/usr/bin/python3
"""Unittest for AirBnB - Console / review
"""
import os
import unittest
import models.review
from models.review import Review


class Test_Base_Reqeriments(unittest.TestCase):
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
