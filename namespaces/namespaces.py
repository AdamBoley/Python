import random
# As standard, Python provides many built in methods
# We can access these anywhere in our application
# We can see what methods are available with:
print(dir(__builtins__))
# We can see that this provides the standard error types, some class methods and methods like print(), slice() and so on
# This is called the Built-In Namespace

four = 4


def string():
    hello = 'hello'
    return hello


# The Global Namespace exists inside each file when it is run by the interpreter
# Each file is called a Module
# Global Namespace includes all non-nested variables, classes and functions
# This excludes any variables and such that exist inside functions
# We can check what objects we can access globally with:
print(globals())
# prints some standard objects, plus the previously-defined variable called four and the function called string
# also prints the imported random module
# When a module is imported, a new namespace is created for it, so there can be several namespaces running at once
# It does not print the variable hello, which exists inside the function, as hello cannot be accessed outside that function
# Note that since Python is run top-to-bottom, if a command to print the contents of the global namespace are placed before an object, that object will not be printed


# A local namespace is created each time a function is executed
# This local namespace includes all of the variables directly nested inside that function
# We can see what objects exist inside each function with:
print(locals())
# Outside of a function, locals() does the same thing as globals()
# To demonstrate:


def add(num1, num2):
    nested_value = 'nested'
    num3 = num1 + num2
    print(nested_value)
    print(num3)
    num4 = 31

    def nested_function(num3, num4):
        print(num3 + num4)
        print(locals())

    nested_function(num3, num4)
    print(locals())


add(6, 14)
# the locals() method prints the function arguments (num1 and num2), and any local variables(nested_value and num3)
# It also prints any nested functions, such as nested_function(), but not any of the variables inside nested_function
# nested_function() has its own namespace generated when it is run.
# the add() function is the enclosing namespace of nested_function()
# the objects of a nested function can be accessed using locals()

# This seems very powerful - you can check what values are being passed to a function!

# all namespaces are dictionaries, with the objects as keys and the values of those objects as the key values

# Scope
# The concept of Scope works similarly to the concept of namespaces
# The 2 are closely linked

# variables inside functions have local scope, and can only be accessed inside their scope
# variables in the global namespace have global scope, and can be accessed anywhere
# Nested functions can access variables inside their parent functions, also called the enclosing scope or enclosing namespace
# However, enclosing functions cannot access variable in child functions

# nested functions can access variables in the enclosing namespace
# however, nested functions cannot modify those variables
# Therefore, the below function throws an error

# def outer_function():
#     enclosing_value = 'Enclosing Value'

#     def nested_function():
#         enclosing_value += 'changed'

#     nested_function()
#     print(enclosing_value)


# outer_function()

# However, we can overcome this restriction using the `nonlocal` keyword:


def enclosing_function():
    var = "value"

    def nested_function():
        nonlocal var
        var = "new_value"

    nested_function()
    print(var)
    # prints new_value, var can be modified


enclosing_function()

# Similarly, we can modify global variables from inside functions using the global keyword:

global_variable = 50


def global_function():
    global global_variable
    global_variable = 70


global_function()
print(global_variable)

# We can also use the global keyword to create global variables in-situ:


def global_variable_creator():
    global var1
    global var2
    var1 = 90
    var2 = 130


global_variable_creator()
print(var1)
print(var2)
# Note that var1 and var2 are not explicitly defined in the global namespace
# however, we can still access them, since they are created in the function with the global keyword

# LEGB
# Python follows a pattern for finding variables
# first, it will check the local namespace and scope
# if the search is unsuccessful, it will search the enclosing scope
# then it will check the global scope
# then it will check the built-in scope
# this is most easily demonstrated like so:

age = 27


def func():
    age = 42

    def inner_func():
        print(age)

    inner_func()


func()
# when called, the functions will print 42
# this is because the variable age is first encountered in the enclosing scope
# since the search for age was successful at this point, print command is executed
# the search does not continue further, so the global instance of age is ignored
