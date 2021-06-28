#!/usr/bin/python3
"""
Unittest for AirBnB - Console / base
"""
import os
import unittest
import models.base_model
from models.base_model import BaseModel


class Test_Base_Reqeriments(unittest.TestCase):
    """Class to test the base_model class requeriments"""

    # Testing pep8 and shebang
    def test_pep8_Base(os_system):
        """PEP8 validation"""
        os_system.assertEqual(os.system("pep8 ./models/base_model.py"), 0)

    def test_pep8_test_base(os_system):
        """PEP8 validation"""
        path = os.system("pep8 tests/test_models/test_base_model.py")
        os_system.assertEqual(path, 0)

    def test_shebang(self):
        """First line contains #!/usr/bin/python3"""
        with open('./models/base_model.py', 'r') as fd:
            x = fd.read()
            line = x.splitlines()
            self.assertEqual(line[0], '#!/usr/bin/python3')

    def test_shebang_test_base(self):
        """First line contains #!/usr/bin/python3"""
        with open('./tests/test_models/test_base_model.py', 'r') as fd:
            x = fd.read()
            line = x.splitlines()
            self.assertEqual(line[0], '#!/usr/bin/python3')

    # Documentation for Module, class and methods exist
    def test_docmodule(self):
        """Module is documented"""
        temp = models.base_model.__doc__
        self.assertTrue(temp is not None and len(temp) > 0)

    def test_docclass(self):
        """Class is documented"""
        temp = BaseModel.__doc__
        self.assertTrue(temp is not None and len(temp) > 0)

    def test_constructor(self):
        """init is documented"""
        temp = BaseModel.__init__.__doc__
        self.assertTrue(temp is not None and len(temp) > 0)

    def test_doc_methods(self):
        """Functions are documented"""
        # save
        temp = BaseModel.save.__doc__
        self.assertTrue(temp is not None and len(temp) > 0)
        # to_dict
        temp = BaseModel.to_dict.__doc__
        self.assertTrue(temp is not None and len(temp) > 0)
        # Str
        temp = BaseModel.__str__.__doc__
        self.assertTrue(temp is not None and len(temp) > 0)
