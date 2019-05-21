import unittest
from selenium import webdriver

class f7(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass

    def test_001(self):
        pass
    def test_002(self):
        pass


if __name__ == '__main__':
   suite=unittest.TestSuite(unittest.makeSuite(f7))
   unittest.TextTestRunner(verbosity=2).run(suite)
