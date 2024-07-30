import abc12
import unittest

# class TestCuboid(unittest.TestCase):
#     def test_volume(self):
#         self.assertAlmostEqual(abc12.cuboid_volume(2),8)
#         self.assertAlmostEqual(abc12.cuboid_volume(1),1)
#         self.assertAlmostEqual(abc12.cuboid_volume(0),0)
#         self.assertAlmostEqual(abc12.cuboid_volume(5.5),166.375)

# unittest.main()
"""
This code defines a unit test case for a function called cuboid_volume.
• The unittest.TestCase class is used to create a test case, and the test_volume method is defined to test the cuboid_volume function.
• Within the test_volume method, four test cases are defined using the self.assertAlmostEqual method.
• This method checks that the actual value returned by cuboid_volume is approximately equal to the expected value (the second argument) with a default tolerance of 7 decimal places.
• For example, the first test case checks that cuboid_volume(2) returns a value that is approximately equal to 8.
• If the actual value returned by cuboid_volume is not within the tolerance of 7 decimal places of the expected value, the test will fail and an error message will be displayed.
• Overall, this code is used to test the correctness of the cuboid_volume function for different input values.

"""
####################################################################

# class TestCuboid(unittest.TestCase):
#     def test_volume(self):
#         self.assertAlmostEqual(abc12.cuboid_volume(2),8)
#         self.assertAlmostEqual(abc12.cuboid_volume(1),1)
#         self.assertAlmostEqual(abc12.cuboid_volume(0),0)
#         self.assertAlmostEqual(abc12.cuboid_volume(5.5),0)

# unittest.main()

##############################################################
class TestCuboid(unittest.TestCase):
    def test_volume(self):
        self.assertAlmostEqual(abc12.cuboid_volume(2),8)
        self.assertAlmostEqual(abc12.cuboid_volume(1),1)
        self.assertAlmostEqual(abc12.cuboid_volume(0),1)

    def test_input_value(self):
        self.assertRaises(TypeError, abc12.cuboid_volume, True)

unittest.main()

"""
This code is a unit test for a function called cuboid_volume which is imported from a module called volume_cuboid.
• The unittest module is imported to create test cases for the function.
• The TestCuboid class is created which inherits from unittest.TestCase.
• Two test methods are defined within this class: test_volume and test_input_value.
• In test_volume, three assertions are made using the assertAlmostEqual method.
• This method checks if the first argument is equal to the second argument up to a certain number of decimal places.
• In this case, it checks if the volume of a cuboid with a length of 2, 1, and 0 is equal to 8, 1, and 1 respectively.
• In test_input_value, an assertion is made using the assertRaises method.
• This method checks if the first argument raises the exception specified in the second argument when called with the remaining arguments.
• In this case, it checks if calling cuboid_volume with a boolean value raises a TypeError.
• Overall, this code tests the cuboid_volume function for correct output and input validation.
"""