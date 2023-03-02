# When we use packages, Python provides a namespace for that package
# This namespace holds all of the functions, classes and variables in that package
# By default, the namespace of a package is the name of that package
# This can be ambiguous or lengthy or could conflict with a custom object that we have defined
# We can get around this by using an alias:
from matplotlib import pyplot as plt

