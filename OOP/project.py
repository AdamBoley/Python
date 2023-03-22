# We will demonstrate inheritance and getters
# First, we create a class of School

class School():

    # standard constructor
    def __init__(self, name, level, numberOfStudents):
        self.name = name
        self.level = level
        self.numberOfStudents = numberOfStudents

    # a series of getters
    def get_name(self):
        print(self.name)

    def get_level(self):
        print(self.level)

    def get_numberOfStudents(self):
        print(self.numberOfStudents)

    # a setter
    def set_numberOfStudents(self, new_number):
        self.numberOfStudents = new_number

    # string representation method
    def __repr__(self):
        return f"{self.name} school is a {self.level} establishment with {self.numberOfStudents} students"


# now we can instantiate a School object:
brackenhale = School("Brackenhale", "High", 500)
brackenhale.get_name()
brackenhale.get_level()
brackenhale.get_numberOfStudents()
brackenhale.set_numberOfStudents(600)
brackenhale.get_numberOfStudents()


# We now want a subclass of PrimarySchool
class PrimarySchool(School):
    # inherited constructor
    def __init__(self, name, numberOfStudents, pickupPolicy):
        # access the parent class' constructor, but default the level to Primary School
        super().__init__(name, "Primary School", numberOfStudents)
        # create a new attribute:
        self.pickupPolicy = pickupPolicy

    # getter
    def get_pickupPolicy(self):
        print(self.pickupPolicy)

    # string representation method that accesses parent class __repr__
    def __repr__(self):
        parent = super().__repr__()
        return parent + ". The Pickup Policy is {pickupPolicy}".format(pickupPolicy=self.pickupPolicy)


# Now we instantiate
birch_hill = PrimarySchool("Birch Hill", 200, "Pickup Allowed")
# note the lack of level - we set this in the class itself
birch_hill.get_name()
birch_hill.get_level()
birch_hill.get_numberOfStudents()
birch_hill.get_pickupPolicy()
# We access the __repr__ method with a print because that method uses return
print(birch_hill)


# And now we create another new class
class HighSchool(School):
    # constructor
    def __init__(self, name, numberOfStudents, sportsTeams):
        # access parent constructor
        super().__init__(name, "High School", numberOfStudents)
        # this time we set a different custom attribute
        self.sportsTeams = sportsTeams
        # sportsTeams is meant to be a list

    # custom getter
    def get_sportsTeams(self):
        print(self.sportsTeams)

    # a different __repr__ override
    def __repr__(self):
        parent = super().__repr__()
        return parent + f". This school has {len(self.sportsTeams)} teams - {self.sportsTeams}."


crowthorne = HighSchool("Crowthorne", 800, ["Rugby", "Football", "Baseball"])
crowthorne.get_name()
crowthorne.get_level()
crowthorne.get_numberOfStudents()
crowthorne.get_sportsTeams()
print(crowthorne)
