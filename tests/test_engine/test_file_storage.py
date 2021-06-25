#!/usr/bin/python3
"""Unittest for AirBnB - Console / file_storage
"""
import os
import unittest
import models.engine.file_storage
from models.engine.file_storage import FileStorage


class Test_Base_Reqeriments(unittest.TestCase):
    """Class to test the file_storage class requeriments"""

    # Testing pep8 and shebang
    def test_pep8_Base(os_system):
        """PEP8 validation"""
        var = "pep8 ./models/engine/file_storage.py"
        os_system.assertEqual(os.system(var), 0)

    def test_pep8_test_base(os_system):
        """PEP8 validation"""
        var= "pep8 tests/test_models/test/test_engine/test_file_storage.py"
        path = os.system(var)
        os_system.assertEqual(path, 0)

    def test_shebang(self):
        """First line contains #!/usr/bin/python3"""
        with open('./models file_storage.py', 'r') as fd:
            x = fd.read()
            line = x.splitlines()
            self.assertEqual(line[0], '#!/usr/bin/python3')

    def test_shebang_test_base(self):
        """First line contains #!/usr/bin/python3"""
        with open('./tests/test_models/test file_storage.py', 'r') as fd:
            x = fd.read()
            line = x.splitlines()
            self.assertEqual(line[0], '#!/usr/bin/python3')

    # Documentation for Module, class and methods exist
    def test_docmodule(self):
        """Module is documented"""
        temp = models.engine.file_storage.__doc__
        self.assertTrue(temp is not None and len(temp) > 0)

    def test_docclass(self):
        """Class is documented"""
        temp = FileStorage.__doc__
        self.assertTrue(temp is not None and len(temp) > 0)

    def test_doc_methods(self):
        """Functions are documented"""
        # all
        temp = FileStorage.all.__doc__
        self.assertTrue(temp is not None and len(temp) > 0)
        # new
        temp = FileStorage.new.__doc__
        self.assertTrue(temp is not None and len(temp) > 0)
        # save
        temp = FileStorage.save.__doc__
        self.assertTrue(temp is not None and len(temp) > 0)
        # reload
        temp = FileStorage.reload.__doc__
        self.assertTrue(temp is not None and len(temp) > 0)
        # to_dictionary
        temp = Rectangle.to_dictionary.__doc__
        self.assertTrue(temp is not None and len(temp) > 0)
