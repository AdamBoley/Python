# demonstration of the split() method
# This method always produces a list of strings

# split at spaces
# By default, split() splits strings around spaces

line_one = "The sky has given over"

line_one_words = line_one.split()

print(line_one_words)

# split around a designated character
# if we supply a designated character, the output list will contain elements split around that character
# Do note that the designated character will be removed, so take care when supplying characters
# we have a string of poorly-formatted names of authors
authors = "Audre Lorde,Gabriela Mistral,Jean Toomer,An Qi,Walt Whitman,Shel Silverstein,Carmen Boullosa,Kamala Suraiyya,Langston Hughes,Adrienne Rich,Nikki Giovanni"

author_names = authors.split(',')

print(author_names)
# returns a list of author names

# now we just want the last names
author_last_names = []
# first, instantiate an empty list to hold our last names

# loop over the author_names list
for element in author_names:
    last_name = element.split()
    # each author name has two words, so we split at the space to create a mini 2-element list
    # print(last_name)
    author_last_names.append(last_name[-1])
    # now append the last element of the mini-list to the author_last_names list

print(author_last_names)

# split at new lines
# Multi-line strings can be split at the new lines

spring_storm_text = \
"""The sky has given over 
its bitterness. 
Out of the dark change 
all day long 
rain falls and falls 
as if it would never end. 
Still the snow keeps 
its hold on the ground. 
But water, water 
from a thousand runnels! 
It collects swiftly, 
dappled with black 
cuts a way for itself 
through green ice in the gutters. 
Drop after drop it falls 
from the withered grass-stems 
of the overhanging embankment."""
# here we have a multi-line string

spring_storm_lines = spring_storm_text.split('\n')
# we designate that we want to split via the new-line escape character

print(spring_storm_lines)
