# Here, we will demonstrate OOP
# Lets create an Employee class, so that we can store various employee data:

class Employee():
    new_id = 1
    # employee id

    def __init__(self):
        self.id = Employee.new_id
        Employee.new_id += 1
        # init method
        # when called, employee is given the current id, and then new_id is incremented

    def say_id(self):
        print("My id is ", self.id)
        # prints employee id


e1 = Employee()
e2 = Employee()
# instantiate Employee objects

e1.say_id()
e2.say_id()
# print ids

# We can now demonstrate inheritance
# we will do this by creating an Admin class that inherits from Employee


class Admin(Employee):
    pass


e3 = Admin()
e3.say_id()
# prints My id is 3
# because Admin inherits all of the methods and attributes of the parent Employee class


# Child classes can inherit some but not all methods from their parent
# We can do this through overrides
# override methods have the same name, but have different behaviour

class Supervisor(Employee):
    def say_id(self):
        print("I am a supervisor")
        # Instead of printing the ID, we print a different string


e4 = Supervisor()

e4.say_id()
# prints I am a supervisor


# When overriding a method, we may still want to access the behaviour of the parent method
# We can do this with super()

class Executive(Employee):
    def say_id(self):
        super().say_id()
        print("I am an executive")


e5 = Executive()

e5.say_id()
# prints "My id is 5" and "I am an executive"


# It is possible for a subclass to inherit from multiple classes at the same time
# This may occur when there are several layers of inheritance
# This is when a class inherits from a parent class, and that parent class has a parent class of its own
# We will demonstrate this by defining a class of Manager, which inherits from Admin

class Manager(Admin):
    def say_id(self):
        super().say_id()
        print("I'm in charge")


e6 = Manager()

e6.say_id()
# prints:
# My id is 4.
# I am an admin.
# I'm in charge


# The other way for a class to have multiple inheritance is for it to directly inherit from 2 or more classes, where there is no chain of inheritance
# We can demonstrate this by creating another class called Support, who are both Admins and Users
# First we need to define the User class:

class User:
    def __init__(self, username, role="Customer"):
        self.username = username
        self.role = role

    def say_user_info(self):
        print("My username is {}".format(self.username))
        print("My role is {}".format(self.role))


# now we can define the Support Class:
class Support(Employee, User):
    def __init__(self):
        super().__init__()
        # In this case, super() points to the first class to inherit from, which is Employee
        User.__init__(self, self.id, "Support")
        # To access the other parent class, we need to indicate it directly
        # We must pass the necessary arguments as well - self.id is User username and "Support" is User role

    def say_id(self):
        super().say_id()
        print("I am a Support Rep.")


e7 = Support()
e7.say_user_info()
# this works because e7 can access the say_user_info method of the User class

# Polymorphism is the concept of applying the same operation to different objects by virtue of identical method names
# This is useful when the type of object may not be known when the program is run
# To demonstrate, we will define an entirely new class for an Auditor, which will not inherit from any extant class
# However, the Auditor class will have the same say_id() method
# this will allow us to do the same operations


class Auditor():
    def say_id(self):
        print("I am an auditor")


# now we instantiate an object:
auditor = Auditor()

# now we can demonstrate polymorphism. First, lets create a list of objects that we want to loop over:
meeting = [e1, e2, e3, e4, e5, e6, e7, auditor]

for attendee in meeting:
    attendee.say_id()


# Dunder methods
# Every class in Python has access to Dunder methods
# Dunder init, __init__() is one
# Dunder methods allow us to change the way operators work
# this is called operator overloading
# We can demonstrate this by overloading the addition operator +:

class Animal:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name

    def __add__(self, another_animal):
        return Animal(self.name + another_animal.name)


a1 = Animal("Horse")
a2 = Animal("Penguin")
# instantiates 2 objects
a3 = a1 + a2
# Normally this wouldn't work, but the __add__() method has changed how the + operator works. It now concatenates strings
print(a1)  # Prints "Horse"
print(a2)  # Prints "Penguin"
print(a3)  # Prints "HorsePenguin"

# We can also overload the len() method
# To do so, we will create a class of Meeting, which contains a list of attendees:


class Meeting:
    def __init__(self):
        self.attendees = []

    def __add__(self, employee):
        print("ID {} added.".format(employee.id))
        self.attendees.append(employee)

    # now we override the len() method to return the number of attendees
    def __len__(self):
        return len(self.attendees)


e10 = Employee()
e11 = Employee()
e12 = Employee()
m1 = Meeting()
# instantiate 3 employees and 1 meeting
m1 + e1
m1 + e2
m1 + e3
# add employees to the meeting
print("The number of attendees is", len(m1))
# print the number of attendees


# Abstraction
# Abstraction is useful when programs become big
# in these cases, classes might start to share functionality and the lines of inheritance may become unclear
# Abstraction defines the behaviours that all classes must share
# We may also want base classes to serve as templates that are inherited from, but that cannot have objects instantiated from them directly
# We'll demonstrate below:
from abc import ABC, abstractmethod


class AbstractEmployee(ABC):
    # This case is a base class that is inherited from
    # however, it cannot directly instantiate objects
    # the class is inherits from, the Abstract Base Class, ABC, does not allow this
    new_id = 1

    def __init__(self):
        self.id = AbstractEmployee.new_id
        AbstractEmployee.new_id += 1

    # the abstractmethod decorator forces all classes that inherit from AbstractEmployee to define a say_id() method
    # an error is raised if not
    @abstractmethod
    def say_id(self):
        pass


# Write your code below
class Senior(AbstractEmployee):
    # Without this method, an error is caused, since AbstractEmployee requires a custom say_id() method to be defined
    def say_id(self):
        print(self.id)


e15 = Senior()
e15.say_id()


# Encapsulation
# Encapsulation is the concept of hiding methods and data inside the object they relate to
# We control access with access modifiers

# Public members can be accessed from anywhere
# Protected members can be accessed from within the same module (file)
# Private members can be accessed from with the same class

# In Python, all members are public, as there isn't any kind of access control
# That said, a common convention is to prefix attributes (variables) that would be protected with an underscore _
# private members can be indicated by prefixing 2 underscores
# Private members undergo a mechanism called name mangling, which modifies their names so that they do not accidentally inherit classes of the same name
# This is an implied notice to other developers to be careful when accessing that member

class Founder():
    def __init__(self):
        self.id = None
        self._id = 100
        self.__id = 1000
# despite having similar names, each of these is a seprate attribute


founder = Founder()
print(dir(founder))
# The dir() method lists all class members
# id and _id will be at the end of the printed list
# __id does not show directly, instead it beomes _Founder__id, at the start of the list


# Getters, Setters and Deleters
# These provide Read, Update and Delete functionality to a class
# getters, setters and deleters expose protected attributes
# using them is the convention because they allow restrictions and other complex behaviour
# using public attributes without getters, setters and deleters would not allow these restrictions


class Officer():
    new_id = 1

    def __init__(self, name=None):
        self.id = Officer.new_id
        Officer.new_id += 1
        self._name = name
        # standard init method

    def get_name(self):
        # getter method
        return self._name

    def set_name(self, new_name):
        # setter method, which updates the name
        self._name = new_name

    def del_name(self):
        # deleter method, which deletes the name
        del self._name


e18 = Officer("Maisy")
e19 = Officer()
# instantiate some objects
# e18 has a valid name
# e19 has no name
print(e18.get_name())
# prints Maisy

e19.set_name("Fluffy")
# updates e19 to have the name Fluffy
print(e19.get_name())

e19.del_name()
# deletes e19's name
print(e19.get_name())
# this throws an error, since e19 no longer has a name