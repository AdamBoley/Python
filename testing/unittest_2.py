# Unittest has built in methods that replace the assert keyword
# Three common ones are 
# assertEqual which checks for equality. Takes 2 arguments and checks if they are equal
# assertIn, which checks for membership, Takes 2 arguments - a variable and a container, and checks if the variable is in the container
# assertTrue, which checks if something evaluates to True. Takes a single argument

# We can demonstrate AssertIn and AssertTrue below:
import unittest
import entertainment


# Write your code below: 
class EntertainmentSystemTests(unittest.TestCase):

    def test_movie_license(self):
        daily_movie = entertainment.get_daily_movie()
        licensed_movies = entertainment.get_licensed_movies()
        self.assertIn(daily_movie, licensed_movies)
        # this test will pass

    def test_wifi_status(self):
        wifi_enabled = entertainment.get_wifi_status()
        self.assertTrue(wifi_enabled)
        # this test will fail


unittest.main()
