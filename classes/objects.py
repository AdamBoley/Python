# Since everything is an object, and all objects have attributes, we can access the attributes of an object at runtime

# Objects have user-defined attributes, and also a great many built-in objects

class Fake:
    pass


fake = Fake()
fake.attribute = "Cool"

print(dir(fake))
# prints the default attributes of classes, plus the user-defined attribute attribute


fun_list = [10, "string", {'abc': True}]

print(type(fun_list))
# Prints <class 'list'>

print(dir(fun_list))
# prints a lot of attributes


print(dir(5))


def this_function_is_an_object():
    return "hello"


print(dir(this_function_is_an_object))
