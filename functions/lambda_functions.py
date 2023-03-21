# Lambda functions are short, one line functions

# Consider the following simple function:


def add_two(my_input):
    return my_input + 2


# We can compress it down to one line like so:

add_two = lambda my_input: my_input + 2

# To break the syntax down:
# add_two is not a variable, but the name of the lambda function
# lambda is a definition, like def or class
# my_input is an argument
# my_input + 2 is what is to be returned
# this actually throws a Flake8 E731 error
# The consensus is not to use Lambda functions this way
# Clear over short, according to PEP8

# Lambda functions can also use conditionals:
check_if_A_grade = lambda grade: 'Got an A!' if grade >= 90 else 'Did not get an A.'
