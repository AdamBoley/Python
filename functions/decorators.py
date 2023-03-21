# Decorators are functions that can add functionality to existing functions

# Recall that functions are objects:

def add_five(num):
    print(num + 5)
# we define a simple function to add 5


# then we call it:
add_five(3)

# The parentheses are necessary to invoke the function
# but they aren't necessary:

add_five
# this doesn't throw a fatal error, its just pointless

print(add_five)
# This prints the location in memory of the function


# Decorators:
# A decorator is a function. We demonstrate below:
# We want to print a name with a title (Mr., Prof., etc)
def title_decorator(print_name_function):
    def wrapper():
        print("Sir")
        print_name_function()
    return wrapper
# this is the decorator function that adds functionality to the functions below


def print_my_name():
    print("Adam")


def print_stuarts_name():
    print("Stuart")

# functions defined


decorated_function_adam = title_decorator(print_my_name)
decorated_function_adam()
# prints Sir and Adam

decorated_function_stuart = title_decorator(print_stuarts_name)
decorated_function_stuart()
# prints Sir and Stuart


# Calling the title_decorator function is quite tedious
# much easier to use a simple decorator:

@title_decorator
def print_kierans_name():
    print("Kieran")


print_kierans_name()
# prints Sir and Kieran, without having to tediously set things up
# all we need to do is call the function as normal


# Decorators with parameters:
# By default, decorator functions don't accept positional arguments
# if we try:

# @title_decorator
# def print_a_name(name):
#     print(name)


# print_a_name("Tom")
# This throws an error


# To get around this, we need to modify the child wrapper function
# a different name is used to avoid repition errors
def lord_decorator(print_name_function):
    def wrapper(*args, **kwargs):
        print("Lord")
        print_name_function(*args, **kwargs)
    return wrapper


@lord_decorator
def print_another_name(name):
    print(name)


print_another_name("Martin")
# prints Lord and Martin
