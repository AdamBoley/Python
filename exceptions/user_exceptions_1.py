# Whilst the built-in exceptions are perfectly valid, they won't always be the most detailed way to describe errors
# to provide detailed error descriptions, we can use custom errors
# custom exceptions are classes tha inherit from the base Exception class

# here we have an inventory of instruments and their stock levels
inventory = {
    'Piano': 3,
    'Lute': 1,
    'Sitar': 2
}


# here we have a custom class for handling inventory errors
class InventoryError(Exception):
    pass


def submit_order(instrument, quantity):
    supply = inventory[instrument]
    
    if quantity > supply:
        raise InventoryError
    else:
        inventory[instrument] -= quantity
        print('Successfully placed order! Remaining supply: ' + str(inventory[instrument]))


instrument = 'Piano'
quantity = 5
submit_order(instrument, quantity)
# this will raise our custom inventory error, as we ordering more pianos than we have in stock