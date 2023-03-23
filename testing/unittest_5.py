# when testing, we may want to use parameterization
# This is useful for testing functions in the same manner but with different parameters
# we might test a multiplier function with certain numbers
# Only the parameters of the tests change, not the way in which we do them
# this helps condense similar tests down into a single test function using a loop
# unittest provides the subTest() method for this, which treats each cycle of the loop as an individual test

import unittest
import entertainment


# This case is similar to unittest_2.py, but we are testing a list of movies rather than 1
class EntertainmentSystemTests(unittest.TestCase):

    def test_movie_license(self):
        daily_movies = entertainment.get_daily_movies()
        licensed_movies = entertainment.get_licensed_movies()
        # define our variables

        # now use a for loop
        for movie in daily_movies:
            print(movie)
            # subTest is necessary to treat each loop as a single test
            # without it, the entire loop is a single test, and so will fail when it encounters a failure case
            with self.subTest():
                self.assertIn(movie, licensed_movies)


unittest.main()
