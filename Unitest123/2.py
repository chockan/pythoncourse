import unittest

class abc(unittest.TestCase):


    @classmethod
    def setUpClass(cls):
        print("setup class method executed")

    def setUp(self):
        print("setUp method execution")
    def test_method1(self):
        print('test method execution')
    def test_method2(self):
        print('test method execution')
        
    def tearDown(self):
        print("tearDown method execution")

    @classmethod
    def tearDownClass(cls):
        print("tearDown class method executed")

unittest.main()