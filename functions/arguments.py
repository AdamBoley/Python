# There are three types of function arguments:
# Positional arguments, where arguments are called by their position in the function defintion
# Keyword arguments, where arguments are called by their name
# Default arguments, where arguments are given default values that can be optionally overridden in function calls

# To demonstrate, consier this function:


def print_name(first_name, last_name):
    print(first_name, last_name)


# Postional arguments:
print_name('Jiho', 'Baggins')
# We map Jiho to first_name and Baggins to last_name
# the order in which we supply the parameters is important

# Keyword arguments:
print_name(last_name='Baggins', first_name='Jiho')
# Here, we specify which parameters map to which arguments, so the order doesn't matter

# Default arguments:
# We specify defalt values


def name(first_name='Jiho', last_name='Baggins'): 
    print(first_name, last_name)


name()

# To demonstrate further:
# We have a dictionary of tables in a restaurent:
tables = {
    1: ['Jiho', False],
    2: [],
    3: [],
    4: [],
    5: [],
    6: [],
    7: [],
}
print(tables)

# We have a function to assign customers to a table:


def assign_table(table_number, name, vip_status=False):
    tables.update({table_number: [name, vip_status]})
    # we use the dictionary update() method


assign_table(6, 'Yoni', False)
print(tables)
# Here we supply all 3 parameters via positional arguments

assign_table(name='Martha', vip_status=True, table_number=3)
print(tables)
# Here we use keyword arguments for better control

assign_table(4, 'Karla')
print(tables)
# Here we rely on the default argument for vip_status so that we don't need to supply that parameter