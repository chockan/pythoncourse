import unittest

# class abc(unittest.TestCase):
#     def setUp(self):
#         print("setUp method execution")
#     def test_method1(self):
#         print('test method execution')
#     def tearDown(self):
#         print("tearDown method execution")

# unittest.main()


###################################################
class abc(unittest.TestCase):
    def setUp(self):
        print("setUp method execution")
    def test_method1(self):
        print('test method execution')
    def test_method2(self):
        print('test method execution')
        
    def tearDown(self):
        print("tearDown method execution")
        print('#'*30)

unittest.main()