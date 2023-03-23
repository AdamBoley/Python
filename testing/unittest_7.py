# Skipping tests
# sometimes we want to skip a test if they should only run in certain conditions
# a good example is consideration of operating system - we may want a test to run only on Linus systems

# We check these conditions with complex decorators, placed above test functions:
# unittest.skipUnless, skips if a condition evaluates to False
# unittest.SkipIf, skips if a condition evaluates to True

# We can also use the skipTest() method, which is placed inside a test function

# Skip decorators are useful if the skip conditions are relatively simple
# the skipTest() method is useful if the conditions are more complex and cannot easily be loaded into a decorator

# we'll demonstrate both approaches below:

import unittest
import entertainment


class EntertainmentSystemTests(unittest.TestCase):

    # this decorator calls the regional_jet() function, which returns true, so the test skips
    @unittest.skipIf(entertainment.regional_jet(), 'Not available on regional jets')
    def test_movie_license(self):
        daily_movie = entertainment.get_daily_movie()
        licensed_movies = entertainment.get_licensed_movies()
        self.assertIn(daily_movie, licensed_movies)

    # this decorator uses the reverse approach - regional_jet evaluates to True, but we preface with not, so the test skips
    @unittest.skipUnless(not entertainment.regional_jet(), 'Not available on regional jets')
    def test_wifi_status(self):
        wifi_enabled = entertainment.get_wifi_status()
        self.assertTrue(wifi_enabled)

    def test_device_temperature(self):
        if entertainment.regional_jet():
            self.skipTest('Not available on regional jets')
        # this if statement checks if regional_jet evaluates to True, and if so, skips the test
        device_temp = entertainment.get_device_temp()
        self.assertLess(device_temp, 35)

    def test_maximum_display_brightness(self):
        if entertainment.regional_jet():
            self.skipTest('Not available on regional jets')
        # same as above
        brightness = entertainment.get_maximum_display_brightness()
        self.assertAlmostEqual(brightness, 400)


unittest.main()
# in the terminal, prints that 4 tests were skipped
