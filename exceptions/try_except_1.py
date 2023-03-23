# Normally, exceptions cause a program to stop executing
# Using the Try / Except syntax allows programs to continue even after an exception occurs
# This is known as exception handling

# This requires at least 2 code blocks - a try block and an except block
# the try block executes preferentially
# if the try block raises an exception, then the except block activates, allowing the program to keep running

# here we have a program to print the number of sales people and managers at various stores, plus the ratio
# the lack of managers at the Melbourne store causes a ZeroDivisionError
staff = {
    'Austin': {
        'floor managers': 1,
        'sales associates': 5
    },
    'Melbourne': {
        'floor managers': 0,
        'sales associates': 8
    },
    'Beijing': {
        'floor managers': 2,
        'sales associates': 5
    },
}


def print_staff_report(location, staff_dict):
    managers = staff_dict['floor managers']
    sales_people = staff_dict['sales associates']
    ratio = sales_people / managers
    print('Instrument World ' + location + ' has:')
    print(str(sales_people) + ' sales employees')
    print(str(managers) + ' floor managers')
    print('The ratio of sales people to managers is ' + str(ratio))
    print()


for location, staff in staff.items():
    try:
        print_staff_report(location, staff)

    except:
        print('Could not print sales report for ' + location)
        # this triggers when the Melbourne store is printed, as it reacts to the ZeroDivisionError and keeps the program running
        # the linter warns that bare except clauses should not be used


# Catching Specific exceptions
# Whilst using generic except clauses is valid, best practice is to use specific exceptions
# Normally, we'll have a good idea of what sort of exceptions our code is likely to raise
# if we add a specific error to the except clause, it will only trigger if that error is raised
# if another error is raised, the except clause won't trigger, so we may need several except clauses to handle multiple exceptions
# when we use specific exceptions, we can capture the exception object using the keyword as
# As we have stored the object, we can do stuff with it
# the convention is to capture the object under the alias e

# To demonstrate, we will modify the for loop slightly:
for location, staff in staff.items():
    try:
        print_staff_report(location, staff)

    except ZeroDivisionError as e:
        print('Could not print sales report for ' + location)
        print(e)
# this actually causes a TypeError - probably something to do with multiple for loops
