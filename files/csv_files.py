# CSV files
# CSV files are just text files with some imposed structure
# This means that they can be read and modified just like text files:

with open('legions.csv') as file:
    text = file.read()
print(text)

# However, if we want to do more complex operations with CSV files, we need the csv library:
import csv

# Now we can open the CSV file
# The DictReader method of the csv library converts lines into python Dictionaries
with open('legions.csv') as file:
    dictionary = csv.DictReader(file)
    for row in dictionary:
        print(row['Specialism'])
        # this prints out each legion's specialism, which is now stored as a key-value pair

# Over time, CSV has come to mean any file where information is separated by a delimiter
# this delimiter can be a comma, or a colon or a semi-colon or anything
# Fortunately, the DictReader method can handle these
# We just need to supply the delimiter as a parameter
# The miltarum.csv file uses colons as delimiters:

specialisms = []
with open('militarum.csv') as file:
    dictionary = csv.DictReader(file, delimiter=':')
    for row in dictionary:
        specialisms.append(row['Specialism'])
print(specialisms)

# We can also use the csv library to add data to a csv file
# To do this, we use DictWriter()

# To demonstrate this, we will write some content to the empty clans.csv file using the list of dictionaries below:
clans = [
    {
        "name": "Goffs",
        "known for": "getting stuck in"
    },
    {
        "name": "Bad Moons",
        "known for": "being well armed" 
    },
    {
        "name": "Evil Sunz",
        "known for": "going very fast"
    },
    {
        "name": "Deathskullz",
        "known for": "loot and plunder"
    },
    {
        "name": "Snakebites",
        "known for": "the old ways"
    },
    {
        "name": "Blood Axes",
        "known for": "being taktikal"
    },
    {
        "name": "Freebooterz",
        "known for": "being competitive"
    },
]

fields = ['name', 'known for']

with open('clans.csv', 'w') as document:
    writer = csv.DictWriter(document, fieldnames=fields)
    writer.writeheader()
    for entry in clans:
        writer.writerow(entry)
# this block transcribes the clans list of dictionaries to the clans.csv file, using fields as the fieldnames

with open('clans.csv') as file:
    dictionary = csv.DictReader(file)
    for row in dictionary:
        print("The " + row['name'] + " are known for " + row['known for'])
# this block prints out the contents, demonstrating that the file has been written to


