# join() is used to fuse strings together
# the syntax is a bit weird:

reapers_line_one_words = ["Black", "reapers", "with", "the", "sound", "of", "steel", "on", "stones"]
# we have a list of individual words that can be joined to make a sentence

reapers_line_one = ' '.join(reapers_line_one_words)
# this is the weird syntax
# join() is a string method, so it must act on a string
# We use a string with a space as the base for the join method

print(reapers_line_one)
# The output is:
# Black reapers with the sound of steel on stones
# note that because we used a string with a space, the list elements are joined together after spaces

# joining with different characters
# the join() method can be used with any string
# a common delimiter is a comma
# this can be used to create a Comma Separated Values file, CSV

santana_songs = ['Oye Como Va', 'Smooth', 'Black Magic Woman', 'Samba Pa Ti', 'Maria Maria']

santana_songs_csv = ','.join(santana_songs)
print(santana_songs_csv)
# => 'Oye Como Va,Smooth,Black Magic Woman,Samba Pa Ti,Maria Maria'

# We can also use a newline escape character:

winter_trees_lines = ['All the complicated details', 'of the attiring and', 'the disattiring are completed!', 'A liquid moon', 'moves gently among', 'the long branches.', 'Thus having prepared their buds', 'against a sure winter', 'the wise trees', 'stand sleeping in the cold.']

winter_trees_full = '\n'.join(winter_trees_lines)
# this joins the elements together to create a multi-line string

print(winter_trees_full)
#output:
# All the complicated details
# of the attiring and
# the disattiring are completed!
# A liquid moon
# moves gently among
# the long branches.
# Thus having prepared their buds
# against a sure winter
# the wise trees
# stand sleeping in the cold.
