# Errors are a fact of life
# Exceptions are a specific type of error
# exceptions occur in syntactically-correct code
# exceptions are runtime errors, as they occur during execution when a piece of code is executed
# a common exception is a NameError, which occurs when you try to use a variable that hasn't been defined
# One feature of Python is the traceback, that points you to the code that caused the error

# We can examine the base classes of any error by using __bases__:
print(NameError.__bases__)
print(SyntaxError.__bases__)
# both of these print Exception, since they are objects that inherit from the built-in Exception class
# we can go one step further:
print(Exception.__bases__)
# prints BaseException, the base class for all exceptions
# The Exception class is publically available, so we can create custom errors
