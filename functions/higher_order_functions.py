# In Python, functions are considered First Class Objects
# This means: 
# that they can be stored as variables
# can be passed as arguments to other functions
# can be returned by functions
# can be stored in data structures

# Store functions in variables:
# Here, we assign a function to a variable
uppercase = str.upper

# And then call it
big_pie = uppercase("pumpkinpie")
print(big_pie)

# Store functions in data structures:
# Here we store two functions in a list
string_manipulation_functions = [str.upper, str.lower]


# Functions as arguments:
# The basic syntax is:
def total_bill(func, value):
    total = func(value)
    return ("The total amount owed is $" + "{:.2f}".format(total) + ". Thank you! :)")
# the function calculates a total for a bill
# the function takes another function as an argument, which is then called
# The return statement formats the output so that it is the same regardless of what function is used
# This follows the DRY principle


# one function that can be called is one for calculating the sales tax:
def add_tax(total):
    tax = total * 0.06
    new_total = total + tax
    return new_total


total_bill(add_tax, 100)


# Of course, it makes little sense to separate out the functions this way unless we have several functions that can be called
# Another we could call is one for calculating the tip:
def add_tip(total):
    tip = total * .2
    new_total = total + tip
    return new_total


total_bill(add_tip, 100)


# This is a basic demonstration
# We can increase the complexity with a loop:
def total_bills(func, list):
    # This list will store all the new bill values
    new_bills = []

    # This loop will iterate through our bills
    for i in range(len(list)):

        # Here we apply the function to each element of the list!
        total = func(list[i])
        new_bills.append("Total amount owed is $" + "{:.2f}".format(total) + ". Thank you! :)")

    return new_bills


# Functions as return values
# below we have a function for calculating the volume of a box:
def make_box_volume_function(height):
    # defines and returns a function that takes two numeric arguments,
    # length &  width, and returns the volume given the input height
    def volume(length, width):
        return length * width * height

    return volume
    # returns the nested volume function
    # volume is now stored as the value of the calling variable


box_volume_height15 = make_box_volume_function(15)
# first we call the wrapping function
# box_volume_height15 is now effectively the volume function with a height of 15
# therefore, that variable can be called with length and width:
print(box_volume_height15(3, 2))
# This particular application is perhaps overly complex, but it is a good demonstration


# Perhaps a better demonstration:

def get_math_function(operation):
    def add(num1, num2):
        return num1 + num2

    def subtract(num1, num2):
        return num1 - num2

    if operation == '+':
        return add
    if operation == '-':
        return subtract
# functions defined
# get_math_function doesn't do much by itself
# it just holds 2 child functions and checks which to return


add_function = get_math_function('+')
# assign a variable
# we can check that add_function is a variable with:
print(add_function)
# prints location in memory

# we can now call add_function as if it were a normal function:
print(add_function(8, 10))
# prints 18


# Built In Higher Order Functions
# Python includes some built in higher-order functions
# Some of these are: map(), filter() and reduce()

# Map
# The syntax for map() is:
# returned_map_object = map(function, iterable)
# map() applies the specified function to each element of the iterable (a list, tuple, etc)

# A basic implementation is:
def double(x):
    return x*2
# first we define a function that we want to use

int_list = [3, 6, 9]
# then we define a data structure that we want to iterate over

doubled = map(double, int_list)
# then we define a variable and assign the map() function

print(doubled)
# this prints the location in memory
# to get the actual list generated:
print(list(doubled))

# map() works well with lambda functions, and this is really the only proper use-case for lambda functions:
doubled = map(lambda input: input*2, int_list)
# This takes advantage of lambda functions being anonymous

print(list(doubled))

# A slightly more complex version:
# We have a list of grades, some are in a 4-point scale and some are in a 100-point scale
# We want all grades to be the 100 point scale

grade_list = [3.5, 3.7, 2.6, 95, 87]

grades_100scale = map(lambda grade: grade * 25 if grade <= 4 else grade, grade_list)
# We use a lambda function to multiple the grades by 25 if they are on the 4-point scale. If not, leave them be
# map() needs to be able to iterate over all of the elements of the list, so the else is necessary to catch grades on the 100-point scale
# Now we convert the map object to a list, because the map object is a new object
updated_grade_list = list(grades_100scale)
# print updated_grade_list:
print(updated_grade_list)

# Filter
# filter() takes a function and an iterable
# it creates a new object that has certain elements filtered out, based on criteria
# below we have a list of names. We want all of the names starting with M or m:
names = ["margarita", "Linda", "Masako", "Maki", "Angela"]

M_names = filter(lambda name: name[0] == "M" or name[0] == "m", names)

print(list(M_names))

# A slightly more complex use-case:
# We have a duplicated list of lists containing authors and a year of publishing
# We want to filter out those lists with integers as the year and retain those with a string as the year:
books = [
    ["Burgess", 1985],
    ["Orwell", "Nineteen Eighty-four"],
    ["Murakami", "1Q85"],
    ["Orwell", 1984],
    ["Burgess", "Nineteen Eighty-five"],
    ["Murakami", 1985]
    ]

string_titles = filter(lambda book: type(book[1]) is str, books)
# Note that we don't need a conditional here, just the criteria that should be checked
# filter is essentially an implied conditional

string_titles_list = list(string_titles)
# print the list string_titles_list
print(string_titles_list)


# Reduce
# reduce works differently to map() and filter()
# It returns a single value
# common uses are to sum all of the elements of the iterable and to multiple the elements together

from functools import reduce
# first, reduce() must be imported

int_list = [3, 6, 9, 12]
# define a list

reduced_int_list = reduce(lambda x, y: x * y, int_list)
# define what we want to do
# reduce multiples 3 and 6, then multiplies that by 9, and that by 12

print(reduced_int_list)
# since reduce produces a single object, there's no need to convert it
# prints 1944, which is 3 * 6 * 9 * 12

# Another application, where we want to join a list of letters:
letters = ['r', 'e', 'd', 'u', 'c', 'e']

word = reduce(lambda x, y: x + y, letters)
# easy - just concatenate the strings
print(word)
