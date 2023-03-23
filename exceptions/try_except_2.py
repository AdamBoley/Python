# An except clause can handle multiple types of exception
# this means that the except clause code will trigger if any of the listed exceptions occur
# we put these exceptions inside a tuple
# an alternative is to use multiple except clauses

instrument_prices = {
    'Banjo': 200,
    'Cello': 1000,
    'Flute': 100,
}


def display_discounted_price(instrument, discount):
    full_price = instrument_prices[instrument]
    discount_percentage = discount / 100
    discounted_price = full_price - (full_price * discount_percentage)
    print("The instrument's discounted price is: " + str(discounted_price))


instrument = 'Banjo'
discount = '20'

# here we use multiple except clauses to capture different exceptions
try:
    display_discounted_price(instrument, discount)
except KeyError:
    print('An invalid instrument was entered!')
except TypeError:
    print('Discount percentage must be a number!')
except Exception:
    print('Hit an exception other than KeyError or TypeError!')
# the final except clause uses the generic exception, which catches all other exceptions
