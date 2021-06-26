#!/usr/bin/python3
"""Unittest for AirBnB - Console / state
"""
import os
import unittest
import models.state
from models.state import State


class Test_Base_Reqeriments(unittest.TestCase):
    """Class to test the state class requeriments"""

    # Testing pep8 and shebang
    def test_pep8_Base(os_system):
        """PEP8 validation"""
        os_system.assertEqual(os.system("pep8 ./models/state.py"), 0)

    def test_pep8_test_base(os_system):
        """PEP8 validation"""
        path = os.system("pep8 tests/test_models/test_state.py")
        os_system.assertEqual(path, 0)

    def test_shebang(self):
        """First line contains #!/usr/bin/python3"""
        with open('./models/state.py', 'r') as fd:
            x = fd.read()
            line = x.splitlines()
            self.assertEqual(line[0], '#!/usr/bin/python3')

    def test_shebang_test_base(self):
        """First line contains #!/usr/bin/python3"""
        with open('./tests/test_models/test_state.py', 'r') as fd:
            x = fd.read()
            line = x.splitlines()
            self.assertEqual(line[0], '#!/usr/bin/python3')

    # Documentation for Module, class and methods exist
    def test_docmodule(self):
        """Module is documented"""
        temp = models.state.__doc__
        self.assertTrue(temp is not None and len(temp) > 0)

    def test_docclass(self):
        """Class is documented"""
        temp = State.__doc__
        self.assertTrue(temp is not None and len(temp) > 0)
