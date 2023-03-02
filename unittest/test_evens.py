import unittest
from evens import even_number_of_evens


class TestEvens(unittest.TestCase):

    def test_throws_error_if_value_passed_in_is_not_list(self):  # this is a Test Case
        self.assertRaises(TypeError, even_number_of_evens, 4)  # This is an individual test
        #  self.assertRaises(TypeError, even_number_of_evens(4) does not work
        # , since the test passes, so use the above syntax to pass in
        # a specific argument to the function, in this case 4
        # This test passes, since the function raises a TypeError if 4 is passed in

    def test_values_in_list(self):
        self.assertEqual(even_number_of_evens([]), False)  # tests if the function returns False when an empty list is passed in
        self.assertEqual(even_number_of_evens([2, 4]), True)  # tests if the function returns True when 2 even numbers are passed in
        self.assertEqual(even_number_of_evens([2]), False)  # tests if the function returns False when only 1 even number is passed in
        self.assertEqual(even_number_of_evens([1, 3, 5]), False)  # tests if the function returns False when only even numbers are passed in


if __name__ == '__main__':
    unittest.main()
