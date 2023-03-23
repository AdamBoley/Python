# individual tests are called unit tests
# these test the smallest units of a program

# imagine that we want to test a single function
# this function is a single piece of code, so it is known as a unit
# for this function, we can write several test cases
# each test case passes the function a specific set of inputs and expects a particular output

# as a simple example, a simple multiplication function might be tested with large numbers, decimals and negative numbers
# here we have a simple function to return the location of the nearest emergency exit

def get_nearest_exit(row_number):
    if row_number < 15:
        location = 'front'
    elif row_number < 30:
        location = 'middle'
    else:
        location = 'back'
    return location


# Now we can define various test cases, each test case being a function:
def test_row_1():
    assert get_nearest_exit(1) == 'front', ('The nearest exit to row 1 is in the front!')


def test_row_20():
    assert get_nearest_exit(20) == 'middle', 'The nearest exit to row 20 is in the middle!'


def test_row_40():
    assert get_nearest_exit(40) == 'back', 'The nearest exit to row 40 is in the back!'

# now we call our test cases
test_row_1()
test_row_20()
test_row_40()