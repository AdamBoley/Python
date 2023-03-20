# We can also supply any number of keyword arguments using the keyword argument unpacking operator, **
# **kwargs is a dictionary
# We have modified the tables dictionary so that order is a dictionary that holds food and drinks separately
tables = {
  1: {
    'name': 'Chioma',
    'vip_status': False,
    'order': {
      'drinks': 'Orange Juice, Apple Juice',
      'food_items': 'Pancakes'
    }
  },
  2: {},
  3: {},
  4: {},
  5: {},
  6: {},
  7: {},
}
print(tables)


def assign_table(table_number, name, vip_status=False): 
    tables[table_number]['name'] = name
    tables[table_number]['vip_status'] = vip_status
    tables[table_number]['order'] = {}


assign_table(2, 'Douglas', True)
print('--- tables with Douglas --- \n', tables)


# Write your code below:
def assign_food_items(table_number, **order_items):
    food = order_items.get('food')
    drinks = order_items.get('drinks')
    print(order_items)
    print(food)
    print(drinks)
    tables[table_number]['order']['food_items'] = food
    tables[table_number]['order']['drinks'] = drinks
# We unpack the order_items dictionary
# We use the get() method to break down the dictionary by its keys


print('\n --- tables after update --- \n')

# Call the function
assign_food_items(2, food='Seabass, Gnocchi, Pizza', drinks='Margarita, Water')

print(tables)


# Note that we have 2 different keyword parameters, which are packed together into a dictionary for later unpacking

# Since **kwargs is a dictionary, standard dictionary indexing methods can be used, such as the values() method
