# Review of Getters, Setters and Deleters
# These provide Read, Update and Delete functionality to a class
# getters, setters and deleters expose protected attributes
# using them is the convention because they allow restrictions and other complex behaviour
# using public attributes without getters, setters and deleters would not allow these restrictions


class Box:
    def __init__(self, weight):
        self.__weight = weight
        # note that weight is private, it has two underscores

    def getWeight(self):
        return self.__weight
        # we can access weight here

    def setWeight(self, weight):
        if weight >= 0:
            self.__weight = weight
        # we can set weight here using some restrictions
        # like input validation


# We can test the input validation like so:
box = Box(10)

box.setWeight(-5)
print(box.getWeight())
# this doesn't work, and the weight is unchanged

box.setWeight(5)
print(box.getWeight())

# Note that we still need to call the methods to benefit from this
# ideally, we want to interact with the weight attribute directly, and still retain the validation

# This is where the property() function comes in

# Lets demonstrate this with a similar class:


class Container:
    def __init__(self, weight):
        self.__weight = weight

    def getWeight(self):
        return self.__weight

    def setWeight(self, weight):
        if weight >= 0:
            self.__weight = weight

    def delWeight(self):
        del self.__weight

    weight = property(getWeight, setWeight, delWeight, "Docstring for the 'weight' property")

# Note that we now have a delWeight method
# the property() function is used to directly modify the weight attribute
# We pass in the getter, setter and deleter methods, plus a docstring
# We can now access and modify the weight attribute directly


container = Container(10)
print(container.weight)
# instantiate an object

container.weight = 5
print(container.weight)
# prints 5, since the setWeight method is being called

container.weight = -5
print(container.weight)
# prints 5, since validation prevents an invalid update

del container.weight
print(container.weight)
# throws error, since weight no longer exists

# using the property() function has made out private attributes publically accessible
# we also no longer need to call class methods, so the syntax is simpler
# but those methods are still being used, since validation is working
# this also helps with DRY - if we were to change the method name in the class, we would have to change the method calls everywhere

# We can go one step further by using the @property decorator
# lets define another class:


class Holder:
    def __init__(self, weight):
        self.__weight = weight

    @property
    def weight(self):
        """Docstring for the 'weight' property"""
        return self.__weight
    # a getter method
    # the @property means that this is to be used as a prefix for the setter and deleter methods

    @weight.setter
    def weight(self, weight):
        if weight >= 0:
            self.__weight = weight
    # we use the method name plus setter to indicate that this is a setter method

    @weight.deleter
    def weight(self):
        del self.__weight
    # we use the method name plus deleter to indicate that this is a deleter method

# note the much simpler, and clearer syntax
# We also retain the simpler interaction syntax:


holder = Holder(10)

holder.weight = 5

del holder.weight
