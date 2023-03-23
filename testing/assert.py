# Testing is essential to creating good software
# All bugs can be found with time and sufficient manual testing
# but this is laborious
# This is where automated tests come in

# Simple tests can be done with the assert keyword
# this is a conditional checker that returns True or False
# If False is returned, an AssertionError is raised

# here we have a dictionary of travel destinations

destinations = {
    'BUD': 'Budapest',
    'CMN': 'Casablanca',
    'IST': 'Istanbul'
}
print('Welcome to Small World Airlines!')
print('What is the airport code of your travel destination?')
destination = 'HND'

# now we assert that the supplied destination is in the destinations dictionary
assert destination in destinations, 'Sorry, Small World currently does not fly to this destination!'
# since assert throws an AssertionError, the program terminates

# this block throws an error, so the program will terminate here
# this makes placement of assert statements key
city_name = destinations[destination]
print('Great! Retrieving information for your flight to ...' + city_name)
