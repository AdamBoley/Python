import unittest
import surfshop


class SurfShopTests(unittest.TestCase):

    def setUp(self):
        self.cart = surfshop.ShoppingCart()
    # set up method to instantiate an empty shopping cart

    def test_add_one_surfboard(self):
        self.assertEqual(self.cart.add_surfboards(1), 'Successfully added 1 surfboard to cart!')
    # simple test to test adding 1 surfboard

    def test_add_two_surfboards(self):
        self.assertEqual(self.cart.add_surfboards(2), 'Successfully added 2 surfboards to cart!')
    # simple test to test adding 2 surfboards

    def test_add_surfboards(self):
        surfboard_numbers = [2, 3, 4]
        for number in surfboard_numbers:
            with self.subTest(number=number):
                # not sure what number=number is necessary for, but fails without it
                # maybe to pass number into subTest loop?
                # like slug=slug in Django?
                self.assertEqual(self.cart.add_surfboards(number), f'Successfully added {number} surfboards to cart!')
                self.cart = surfshop.ShoppingCart()
                # necessary to reset cart, otherwise cart fills up to over limit, which causes subsequent tests to fail
                # suspect that these are not independent tests, but rather subtests, so the setUp method is not called between each

    def test_too_many_surfboards(self):
        self.assertRaises(surfshop.TooManyBoardsError, self.cart.add_surfboards, 5)
        # pay attention to the different syntax for the assertEquals and assertRaises
        # this test passes, in spite of the operation raising an error

    # @unittest.expectedFailure
    # commented out because the starting code for apply_locals_discount method did not work, so we needed to expect failure
    def test_locals_discount(self):
        self.assertTrue(self.cart.apply_locals_discount)


unittest.main()
