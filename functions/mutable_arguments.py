# Functions can be written with default arguments
# These arguments have default values that are used if no parameter is supplied
# If we try to pass an empty list [] as a default argument
# Consider a simple function to create a Student profile that holds their name, age and grades:


def createStudent(name, age, grades=[]):
    return {
        'name': name,
        'age': age,
        'grades': grades
    }


# We can instantiate these profiles like so:
chrisley = createStudent('Chrisley', 15)
dallas = createStudent('Dallas', 16)
# We pass in the name and age, leaving the scores blank

# We can then have a function that appends grades to the grade list in the dictionary:


def AddGrade(student, grade):
    student['grades'].append(grade)
    # To help visualize the grades we have added a print statement
    print(student['grades'])


# We can now add some grade:
AddGrade(chrisley, 90)
AddGrade(dallas, 100)

# We expect:
# [90]
# [100]

# But we actually get:
# [90]
# [90, 100]

# This is a counter-intuitive feature if Python
# It comes from certain data structures being immutable and certain other data structures being mutable
# Lists are mutable, as are dictionaries and sets
# tuples, integers, floats and strings are immutable
# Default values in functions are executed once, when the function is called the first time
# Any default values are then used for all subsequent function calls, resulting in the output above
# The default list will be the same memory object
# We can check this with:
print(id(chrisley['grades']))
print(id(dallas['grades']))
# We see that both grades keys have the same location in memory, meaning that they are the same memory object
# This means that the same grades list is being modified

# We can work around this by taking advantage of Python's ability to redefine variables:
# (We use different variable names because its the same file)


def create_employee(name, age, rank=None):
    if rank is None:
        rank = []
    return {
        'name': name,
        'age': age,
        'rank': rank
    }


def add_rank(employee, rank):
    employee['rank'].append(rank)
    # To help visualize the ranks we have added a print statement
    print(employee['rank'])


chrisley = create_employee('Chrisley', 15)
dallas = create_employee('Dallas', 16)

add_rank(chrisley, 90)
add_rank(dallas, 100)

# We now get the expected output