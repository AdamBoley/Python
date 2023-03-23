# the else clause is useful if we want to run some code if an exception is NOT encountered
# i.e. what should happen when code runs normally

# This may seem a bit of a roundabout way of writing the code
# However, the Python documentation recommends this approach over adding code to the try clause
# This approach avoid accidentally catching an exception that wasn't raised by the code being protected by the try clause
# A demonstration - say we have a login system:
# dummy functions
def check_password():
    pass


def login_user():
    pass


try:
    check_password()
except ValueError:
    print('Wrong Password! Try again!')
else:
    login_user()


# We could just as easily write:
try:
    check_password()
    login_user()
    # 20 other lines of imaginary code
except ValueError:
    print('Wrong Password! Try again!')

# this approach is valid, but if any of the other code below login_user() raises a ValueError, a misleading statement will be printed
# This will prove challenging to debug

# a more complex demonstration:
customer_rewards = {
    'Zoltan': 82570,
    'Guadalupe': 29850,
    'Mario': 17849
}


def display_rewards_account(customer):

    try:
        rewards_number = customer_rewards[customer]
    except KeyError:
        print('Customer was not found in rewards program!')
    else:
        print('Rewards account number is: ' + str(rewards_number))
# if the else code were instead in the try block, errors could happen and go uncaught


customer_1 = 'Zuigly'
display_rewards_account(customer_1)
# will raise a KeyError

customer_2 = 'Mario'
display_rewards_account(customer_2)
# will work as expected
