# Raising Exceptions:
# we can force a program to raise an error when Python would not normally throw one
# We do this whenever we think a mistake will occur in the program
# rather than continuing on, the error will stop program execution and provide an error message
# We can raise either a specific named exception or a generic exception using the Exception class
# Either approach can be supplied with an error message as a string
# This is a simple demonstration:

instrument_catalog = {
    'Marimba': 1999,
    'Kora': 499,
    'Flute': 899
}
# we have a dictionary of instruments and their prices


def print_instrument_price(instrument):

    if instrument in instrument_catalog:
        print('The price of a ' + instrument + ' is ' + str(instrument_catalog[instrument]))
    else:
        raise KeyError(instrument + ' is not found in instrument catalog!')
# this function prints the price of an instrument
# It has a simple conditional that checks if the supplied instrument is in the catalog
# if not, it raises a standard KeyError with a custom message


print_instrument_price('Marimba')
print_instrument_price('Flute')
print_instrument_price('Piano')
# this is where the KeyError will trigger, since Piano is not a key in the catalog
