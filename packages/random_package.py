# The random package is used in situations where random numbers or choices are useful

import random

# We want to create a list of random numbers 100 elements long, with each number between 1 and 100:
# we do this with the randint() method and a list comprehension:
random_list = [random.randint(1, 100) for i in range(101)]

# this is the same as:
random_list_2 = []
for number in range(101):
    random_list_2.append(random.randint(1, 100))

print(random_list)
print(random_list_2)

print(len(random_list))
print(len(random_list_2))

# we can grab a random choice from these lists using random.choice():
random_choice = random.choice(random_list)

print(random_choice)

# If we want a random sampling of numbers, we can use random.sample():

numbers = random.sample(range(1000), 12)
# this produces a list 12 elements long, with values betwen 0 and 999, since range is exclusive

print(numbers)
