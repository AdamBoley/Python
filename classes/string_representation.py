# String representation
# Another dunder method for classes is __repr__()
# This returns a string representation of an object
# Works similar to the Django magic string method?

class Circle:
    pi = 3.14

    def __init__(self, diameter):
        self.radius = diameter / 2

    def area(self):
        return self.pi * self.radius ** 2

    def circumference(self):
        return self.pi * 2 * self.radius

    def __repr__(self):
        return "Circle with radius {radius}".format(radius=self.radius)


medium_pizza = Circle(12)
teaching_table = Circle(36)
round_room = Circle(11460)

print(medium_pizza)
# prints Circle with radius 6.0

print(teaching_table)
# Circle with radius 18.0

print(round_room)
# Circle with radius 5730.0
