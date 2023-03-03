# Here we will demonstrate 2 classes interacting with each other
# First we define a class of Student, with a constructor and an add_grade function:


class Student:
    def __init__(self, name, year):
        self.name = name
        self.year = year
        self.grades = []

    def add_grade(self, grade):
        if type(grade) is Grade:
            self.grades.append(grade)
        else:
            pass


# now we define some students, and pass in specific data
roger = Student("Roger van der Weyden", 10)
sandro = Student("Sandro Botticelli", 12)
pieter = Student("Pieter Bruegel the Elder", 8)


# now we define a class of Grade, with a class attribute of minimum_passing, to represent a minimum passing grade
class Grade:
    minimum_passing = 65

    def __init__(self, score):
        self.score = score

# now we instantiate a instance of Grade, with a score
pieters_grade = Grade(100)

# now we use the class method add_grade that pieter possesses to add pieters_grade to the pieter variable
pieter.add_grade(pieters_grade)
