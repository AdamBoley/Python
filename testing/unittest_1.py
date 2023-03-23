# the previous approach of defining test case functions is a valid way of writing tests
# however, as code complexity increases, the number and complexity of tests must also increase
# By default, we must call test cases individually, which is laborious
# We may also want to group tests together
# And if a test fails, all subsequent tests won't run

# This is where the unittest module comes in

# unittest is part of the standard library, but must be imported:
import unittest


# We have the same function as before that checks for the nearest exit
def get_nearest_exit(row_number):
    if row_number < 15:
        location = 'front'
    elif row_number < 30:
        location = 'middle'
    else:
        location = 'back'
    return location


# To use unittest, we need to create a class to hold the tests
# this class inherits from the TestCase base class
# this class tests one function
class NearestExitTests(unittest.TestCase):

    # We can now group several test case functions together
    # note the modified syntax
    # instead of assert, we use self.assertEqual, and the statement is wrapped in brackets
    # we don't use a comparison, just the function to test with any function arguments, the expected output and an optional message
    def test_row_1(self):
        self.assertEqual(get_nearest_exit(1), 'front', 'The nearest exit to row 1 is in the front!')

    def test_row_20(self):
        self.assertEqual(get_nearest_exit(20), 'middle', 'The nearest exit to row 20 is in the middle!')

    def test_row_40(self):
        self.assertEqual(get_nearest_exit(40), 'back', 'The nearest exit to row 40 is in the back!')


if __name__ == '__main__':
    unittest.main()
# Instead of calling all of the test case functions separately, we call them all with this line
# unittest will then work its magic behind the scenes
# A report will be printed to the console
