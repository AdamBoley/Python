# Dictionaries are unordered sets of key-value pairs

sensors = {"living room": 21, "kitchen": 23, "bedroom": 20, "pantry": 22}
# sensors hold temperature data from temperature probes

num_cameras = {"backyard": 6,  "garage": 2, "driveway": 1}
# num_cameras holds the number of security cameras in each room

print(sensors)
print(num_cameras)

# The keys can be either strings or numbers
# the values can be any data-type

person = {
    "name": "Shuri",
    "age": 18,
    "family": ["T'Chaka", "Ramonda"]
    }
# person is a good example the values are a string, a number and a list

# we cannot use lists or dictionaries as keys
# this is because keys must be hashable
# a hash value is a specific identifier
# since dictionaries and lists can be modified, any hash value would be unreliable
# Tuples are unmodifiable data structures, so they can be used as keys
# This is useful in niche applications like storing grid coordinates

# Like any other data structure, we can instantiate empty dictionaries that we will fill later
animals_in_zoo = {}

# we can append key-value pairs to dictionaries like so:
animals_in_zoo["zebras"] = 8

animals_in_zoo["monkeys"] = 12

animals_in_zoo["dinosaurs"] = 0

print(animals_in_zoo)

# this is a bit unwieldy
# we can updare a dictionary with several key-value pairs at once with the update method:

user_ids = {"teraCoder": 9018293, "proProgrammer": 119238}

user_ids.update({"theLooper": 138475, "stringQueen": 85739})

print(user_ids)
# will output a dictionary with 4 key-value pairs

# We can change the value of a key in a similar way:
oscar_winners = {
    "Best Picture": "La La Land",
    "Best Actor": "Casey Affleck",
    "Best Actress": "Emma Stone",
    "Animated Feature": "Zootopia"
}

# we target the existing key "Best Picture" and override its value
oscar_winners["Best Picture"] = "Moonlight"

# We can make dictionaries from 2 constituent lists using a Dictionary Comprehension:

drinks = ["espresso", "chai", "decaf", "drip"]
caffeine = [64, 40, 0, 120]
# These are the 2 lists that will be used to make the dictionary

# This is the iterator of pairs - a tuple with the zip() method
# This iterator specifies the lists that are to be combined:
zipped_drinks = zip(drinks, caffeine)

drinks_to_caffeine = {key: value for key, value in zipped_drinks}
# This is how we do a dictionary comprehension, much like a list comprehension
# we could also structure it like so:
# drinks_to_caffeine = {key: value for key, value in zip(drinks, caffeine)}

# The Python Linter makes a recommendation that the above code is unnecessary
# We can use the dict() method:
drinks_to_caffeine_1 = dict(zipped_drinks)

print(drinks_to_caffeine)
print(drinks_to_caffeine_1)

# Get a key:
# We can get the value of a particular key with square bracket notation:
 
zodiac_elements = {
    "water": ["Cancer", "Scorpio", "Pisces"],
    "fire": ["Aries", "Leo", "Sagittarius"],
    "earth": ["Taurus", "Virgo", "Capricorn"],
    "air": ["Gemini", "Libra", "Aquarius"]
    }

print(zodiac_elements["earth"])
# prints ["Taurus", "Virgo", "Capricorn"]

print(zodiac_elements["fire"])
# prints ["Aries", "Leo", "Sagittarius"]

# If we have a situation where we are not sure if a key exists, we can use an IF statement to check if it does, and if so, perform some operation:

if "energy" in zodiac_elements:
    print(zodiac_elements["energy"])

# This is a useful bit of defensive programming - because the "energy" key does not exist in the dictionary, the code will break when we try to run it without the If statement

# An alternative method is to use the get() method:

invalid = zodiac_elements.get("energy")

print(invalid)
# This will print None, since "energy" is not a valid key

# We can also specify the returned value, if None is not useeful:

invalid_default = zodiac_elements.get("energy", "Invalid")

print(invalid_default)
# This will print "Invalid"

# We can delete a key-value pair using the pop() method
# below, we have an inventory of items that can replenish a player's health

available_items = {
    "health potion": 10,
    "cake of the cure": 5,
    "green elixir": 20,
    "strength sandwich": 25,
    "stamina grains": 15,
    "power stew": 30
}

health_points = 20

# these commands will add the value of the specified key to health_points
health_points += available_items.pop("stamina grains", 0)

health_points += available_items.pop("power stew", 0)

# mystic bread does not exist, so 0 will be added to health points
health_points += available_items.pop("mystic bread", 0)

print(available_items)
print(health_points)

# We can get a list of all of the keys of a dictionary with the list() method:

test_scores = {
    "Grace": [80, 72, 90],
    "Jeffrey": [88, 68, 81],
    "Sylvia": [80, 82, 84],
    "Pedro": [98, 96, 95],
    "Martin": [78, 80, 78],
    "Dina": [64, 60, 75]
}
# we can grab the keys as a list like so:
names = list(test_scores)
print(names)

# this list is a separate object and can be modified

# We can get an immutable read-only object using the keys() method:

user_ids = {
    "teraCoder": 100019,
    "pythonGuy": 182921,
    "samTheJavaMaam": 123112,
    "lyleLoop": 102931,
    "keysmithKeith": 129384}

num_exercises = {
    "functions": 10,
    "syntax": 13,
    "control flow": 15,
    "loops": 22,
    "lists": 19,
    "classes": 18,
    "dictionaries": 18
}

users = user_ids.keys()

lessons = num_exercises.keys()

print(users)
# prints dict_keys(['teraCoder', 'pythonGuy', 'samTheJavaMaam', 'lyleLoop', 'keysmithKeith'])

print(lessons)
# prints dict_keys(['functions', 'syntax', 'control flow', 'loops', 'lists', 'classes', 'dictionaries'])


# We can do the same thing for a dictionary's values:

values = num_exercises.values()
print(values)
# prints dict_values([10, 13, 15, 22, 19, 18, 18])

# There is no build-in method for getting the values of a dictionary as a list, but there is a work-around:
list_values = list(num_exercises.values())
print(list_values)

# We can get the keys and values of a dictionary in a list of tuples like so:
pct_women_in_occupation = {
    "CEO": 28,
    "Engineering Manager": 9,
    "Pharmacist": 58,
    "Physician": 40,
    "Lawyer": 37,
    "Aerospace Engineer": 9
}

for key, value in pct_women_in_occupation.items():
    print("Women make up " + str(value) + " percent of " + key + "s")

# The code below combines the pop() method with the items() method:
tarot = {
    1: "The Magician",
    2: "The High Priestess",
    3: "The Empress",
    4: "The Emperor",
    5: "The Hierophant",
    6: "The Lovers",
    7: "The Chariot",
    8: "Strength",
    9: "The Hermit",
    10: "Wheel of Fortune",
    11:	"Justice",
    12:	"The Hanged Man",
    13:	"Death",
    14:	"Temperance",
    15:	"The Devil",
    16:	"The Tower",
    17:	"The Star",
    18:	"The Moon",
    19:	"The Sun",
    20:	"Judgement",
    21:	"The World",
    22: "The Fool"
}

spread = {}

spread["past"] = tarot.pop(13)
spread["present"] = tarot.pop(22)
spread["future"] = tarot.pop(10)

for key, value in spread.items():
    print("Your " + key + " is the " + value + " card.")

# This demonstrates a good way of moving key-value pairs from one dictionary to another
