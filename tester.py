import sys
import os

PROJ_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, PROJ_DIR)

import unittest

import startup.test_interface
import startup.get.methods.test_from_file
import startup.get.methods.test_from_web

loader = unittest.TestLoader()
suite = unittest.TestSuite()

suite.addTests(loader.loadTestsFromModule(startup.test_interface))
suite.addTests(loader.loadTestsFromModule(startup.get.methods.test_from_file))
suite.addTests(loader.loadTestsFromModule(startup.get.methods.test_from_web))

runner = unittest.TextTestRunner(verbosity=3)
result = runner.run(suite)
