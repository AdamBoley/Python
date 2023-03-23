# Test Fixtures

# Tests need to occur in a known state
# if test conditions are uncontrolled, then we could get false negatives and false positives

# A test fixture ensures that tests are set up properly, and torn down properly
# this ensures reliable conditions

# the unittest module does not provide these methods, but will recognise methods named setUp() and tearDown()
# setUp() methods can also be used to gather necessary data prior to tests

# This is complex:

import unittest
import kiosk
# imports companion file


class CheckInKioskTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        kiosk.power_on_kiosk()
    # This is a class method, per its decorator
    # This is a standard bit of Python
    # class methods run once when the class is instantiated
    # In this case, the kiosk is powered on once

    def setUp(self):
        kiosk.return_to_welcome_page()
    # setUp is a standard method that unittest looks for
    # it runs prior to each test
    # it basically resets the program to a state which we want the tests to run on
    # in this case, it returns the kiosk to the welcome page

    def test_check_in_with_flight_number(self):
        print('Testing the check-in process based on flight number')
    # these are our actual tests

    def test_check_in_with_passport(self):
        print('Testing the check-in process based on passport')

    @classmethod
    def tearDownClass(cls):
        kiosk.power_off_kiosk()
    # this is a second class method, per its decorator
    # it runs once all tests are completed


unittest.main()
