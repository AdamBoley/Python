# since our custom errors are classes, they can take attributes (class variables) and methods (class functions)
# We have the same situation as with the user_exceptions_1 file, but we're expanding the custom error class:

class InventoryError(Exception):
    # standard init constructor to set supply attribute
    def __init__(self, supply):
        self.supply = supply

    # str method to return a string
    def __str__(self):
        return 'Available supply is only ' + str(self.supply)


inventory = {
  'Piano': 3,
  'Lute': 1,
  'Sitar': 2
}


def submit_order(instrument, quantity):
    supply = inventory[instrument]

    if quantity > supply:
        raise InventoryError(supply)
        # here we modify our custom error handling to pass in the supply variable, which is stored as a class attribute

    else:
        inventory[instrument] -= quantity
        print('Successfully placed order! Remaining supply: ' + str(inventory[instrument]))


instrument = 'Piano'
quantity = 5
submit_order(instrument, quantity)
