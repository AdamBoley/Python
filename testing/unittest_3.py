# Often, we need to test functions that deal in numerical data
# We have 2 methods to use here:
# assertLess, which takes 2 values and checks to see if one is less than the other
# assertAlmostEqual, which takes 2 values and checks to see if their different to 7DP is 0
# assertAlmostEqual is useful when assertEqual is too strict

import unittest
import entertainment


class EntertainmentSystemTests(unittest.TestCase):

    def test_maximum_display_brightness(self):
        brightness = entertainment.get_maximum_display_brightness()
        self.assertAlmostEqual(brightness, 400)
        # passes as brightness is 399.9999999

    def test_device_temperature(self):
        device_temp = entertainment.get_device_temp()
        self.assertLess(device_temp, 35)
        # fails, as device_temp evaluates to 40


unittest.main()
