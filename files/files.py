# we can open, modify and save files using the with keyword and the open() method:

with open('welcome.txt') as text_file:
    text_data = text_file.read()
print(text_data)
# prints Hello, since Hello is the contents of welcome.txt
# The read() method used above stores the entire document as a string

# We may want to access individual lines in the document
# we can do this using the readlines() method

with open('ork_chanting.txt') as lines_doc:
    for line in lines_doc.readlines():
        print(line)

# Sometimes we may want to read a single line
# for this, we use readline()

with open('ork_chanting.txt') as lines_doc:
    first_line = lines_doc.readline()
    second_line = lines_doc.readline()
    third_line = lines_doc.readline()
    fourth_line = lines_doc.readline()
    fifth_line = lines_doc.readline()
    sixth_line = lines_doc.readline()
    seventh_line = lines_doc.readline()

# each use of readline() strips off one line of the document
# subsequent uses of readline() after all lines have been stripped off will return an empty string

print(first_line)
print(second_line)
print(third_line)
print(fourth_line)
print(fifth_line)
print(sixth_line)
print(seventh_line)
# the print statements print the entire document one line at a time
# the seventh_line variable is an empty string, so it will not visible when printed

# We can modify a file's contents as well, using a variant of the open() method:

with open('welcome.txt', 'w') as doc:
    doc.write('Goodbye')


with open('welcome.txt') as doc:
    text = doc.read()
print(text)

# the 'w' as the second argument allow us to modify the file
# the write() method overrides any extant content of the file
# also, once a document has been written too, it appears that it cannot be read
# Therefore, another with open() statement is needed to read and print the contents of the file
# When we do so, Goodbye will be printed

# To append data to a file without overwriting, we can supply 'a' instead of 'w':
# To demonstate this, first we'll restore the contents of welcome.txt:

with open('welcome.txt', 'w') as doc:
    doc.write('Hello\n')

# now we can append some text:
with open('welcome.txt', 'a') as doc:
    doc.write('Goodbye')

# now we can print the contents:
with open('welcome.txt') as doc:
    text = doc.read()
print(text)
# prints Hello and then Goodbye on a new line

# The with open() syntax is a newer way of opening a file
# The old way involved opening a file, doing something and then closing it again

# there were problems with this, so the new syntax is preferred

