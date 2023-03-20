# Python supports the unpacking operator *
# This allows us to supply any number of positional arguments to a function
# The print function uses this:
print('This', 'is', 'the', 'print', 'function')
# print() doesn't care how many arguments are supplied to it

# We can demonstrate this:


def print_order(*order_items):
    print(order_items)


print_order('Orange Juice', 'Apple Juice', 'Scrambled Eggs', 'Pancakes')
print_order('Poached Eggs', 'Toast')
print_order('Roast Beef', 'Red Wine', 'Gravy', 'Carrots', 'Potatoes', 'Brussel Sprouts')
# The print_order function doesn't care how many parameters we supply
# It works with 2 parameters or a thousand

# We can also use the unpacking operator in loops, since the unpacked variable is a tuple:
tables = {
    1: {
        'name': 'Jiho',
        'vip_status': False,
        'order': 'Orange Juice, Apple Juice'
    },
    2: {},
    3: {},
    4: {},
    5: {},
    6: {},
    7: {},
}
print(tables)
# We have a tables dictionary


# We have a function that updates the tables dictionary
def assign_table(table_number, name, vip_status=False): 
    tables[table_number]['name'] = name
    tables[table_number]['vip_status'] = vip_status
    tables[table_number]['order'] = ''


# We have a function to update the table with the items the customer wants to order
# This also prints the items for the kitchen
def assign_and_print_order(table_number, *order_items):
    tables[table_number]['order'] = order_items
    for item in order_items:
        print(item)


# We call the functions
assign_table(2, 'Arwa', True)
# This call supplies 4 parameters, but the function accepts 2. The first parameter is mapped to the table_number argument, and the rest are packed into a tuple for subsequent unpacking
assign_and_print_order(2, 'Steak', 'Seabass', 'Wine Bottle')
print(tables)

