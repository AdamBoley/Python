# find() takes a single argument and returns the first index value of that argument.
# if a multi-character string is supplied, the index of the first character is returned

# Here we have a line of text and want to know the index at which 'disown' appears:
god_wills_it_line_one = "The very earth will disown you"

disown_placement = god_wills_it_line_one.find('disown')

print(disown_placement)
# prints 20, as the 'd' of 'disown' is at index 20
