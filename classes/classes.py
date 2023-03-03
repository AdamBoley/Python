# Classes

# Classes work a bit like functions
# They don't do anything by themselves
# They must be instantiated before they work
# This is much like how a function must be called

# We do this like so:

# Create the class:
class Legion:
    pass
# pass is used only to avoid an indentation error

# Now we instantiate the class:


legion = Legion()

# legion is an object, instantiated from the Legion() class

# The type() method does the opposite - it returns the class that an object was instantiated from:
print(type(legion))
# returns <class '__main__.Legion'>
# The capital L indicates that legion is an object instantiated from the Legion class
# __main__ means that this is the file we're currently running


# When we instantiate a class, we may want every instance to include the same data
# We do this with a class variable:

class TacticalMarine:
    weapon = "boltgun"

# we have created the TacticalMarine class. All instances of this class will have a weapon of boltgun


# Classes can have methods attached to them. All instances of that class can use those methods
# methods are just functions, but are called methods because they exist with classes
# All class methods must have at least one argument
# convention dictates that we call this argument 'self'
# self refers to the parent class

class AssaultMarine:
    weapon = "chainsword"

    def description(self):
        print("Assault Marines use {}'s".format(self.weapon))

# here we declare the AssaultMarine class and use a description method to print a string that injects the class variable "weapon"

# Class methods can take several arguments
# Below, we declare a class called Circle, which has a class method that calculates the area of a circle


class Circle:
    pi = 3.14

    def area(self, radius):
        area = self.pi * radius ** 2
        return area
# now that Circle has been declared, we can instantiate it:


circle = Circle()

# We can now access the area class method to calculate various areas based on diameters
pizza_area = circle.area(12/2)
teaching_table_area = circle.area(36/2)
round_room_area = circle.area(11460/2)


# Magic Methods
# One common Magic method is the __init__() method
# This method is called whenever we instantiate a new instance of the parent class

# Because the __int__() method is called whenever the class is instantiated, it is called a constructor

# Because __init__() is a method, it can take arguments


class Sphere:
    pi = 3.14

    # Add constructor here:
    def __init__(self, diameter):
        print("New sphere with diameter: {diameter}".format(diameter=diameter))
        # we pass diameter as an argument to __init__()


teaching_table = Sphere(36)
# Note the simplified syntax
# we don't need to instantiate Sphere and then make copies of it as we did with Circle
# This is print New sphere with diameter: 36

# Instance variables
# When we instantiate a class, we may want additional variables
# These are called instance variables, since they are created for a particular instance, not the class as a whole

# Below we have a class of Store:


class Store:
    pass


# Now we instantiate 2 instances of Store
alternative_rocks = Store()
isabelles_ices = Store()

# Now we create and assign instance variables for each instance of Store:
alternative_rocks.store_name = "Alternative Rocks"
isabelles_ices.store_name = "Isabelle's Ices"


# We can access class variables and instance variables similarly

# If we try to access a variable for an instance that does not exist, Python will throw an AttributeError

# One way to guard against this is to use the hasattr() method:
# We can demonstrate this with a list containing elements of various data types:

can_we_count_it = [
  {'s': False},
  "sassafrass",
  18,
  ["a", "c", "s", "d", "s"]
]

# now we can loop over the list:
for element in can_we_count_it:
    if hasattr(element, "count"):
        print(str(type(element)) + " has the count attribute!")
    else:
        print(str(type(element)) + " does not have the count attribute :(")
