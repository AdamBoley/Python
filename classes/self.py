# SELF

# The self keyword is used to create instance variables that are rigid
# These instance variables then effectively become class variables and can be accessed by other methods
# first we define a Circle class:


class Circle:
    pi = 3.14
    # pi is a defined class variable

    def __init__(self, diameter):
        print("Creating circle with diameter {d}".format(d=diameter))
        # Add assignment for self.radius here:
        self.radius = diameter / 2
        # radius is a rigid instance variable, but the self makes it like a class variable

    def circumference(self):
        circumference = 2 * self.pi * self.radius
        # the circumference method can access both the pi class variable and the rigid instance variable radius
        return circumference


# we can now instantiate three instances of Circle:
medium_pizza = Circle(12)
teaching_table = Circle(36)
round_room = Circle(11460)

# And access the circumference method of them:
print(medium_pizza.circumference())
print(teaching_table.circumference())
print(round_room.circumference())
