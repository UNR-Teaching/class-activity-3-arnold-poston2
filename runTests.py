import unittest
loader = unittest.TestLoader()
start_dir = './'
suite = loader.discover(start_dir, "*Tests.py")

runner = unittest.TextTestRunner()
runner.run(suite)