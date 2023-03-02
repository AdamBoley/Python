# the format() method is a way of including variables in a string
# curly braces {} are used as placeholders for these variables
# format takes as many arguments are there are curly braces in the string
# format is best paired with a function:


def poem_title_card(title, poet):
    string = 'The poem "{}" is written by {}.'.format(title, poet)
    return string


print(poem_title_card("I Hear America Singing", "Walt Whitman"))
# outputs: The poem "I Hear America Singing" is written by Walt Whitman.

# One of the problems with format() as above is that the arguments supplied to format must be supplied in the order you want to use them in
# alternatively, the string must be written in such a way that the arguments are used in a particular order

# To counter this, we can fill the curly braces with the particular variable we want to use:


def favorite_song_statement(song, artist):
    return "My favorite song is {song} by {artist}.".format(song=song, artist=artist)
    # alternatively, we can use:
    # return "My favorite song is {track} by {composer}.".format(track=song, composer=artist)
    # to separate the variables


print(favorite_song_statement("Drill", "Frank Klepacki"))

# This allows us to supply the arguments in any order:


def poem_description(publishing_date, author, title, original_work):
    poem_desc = "The poem {title} by {author} was originally published in {original_work} in {publishing_date}.".format(publishing_date=publishing_date, author=author, title=title, original_work=original_work)
    return poem_desc


my_beard_description = poem_description(
    author="Shel Silverstein",
    title="My Beard",
    original_work="Where the Sidewalk Ends",
    publishing_date="1974")
# note that we are supplying the arguments in a different order, but this will still work

print(my_beard_description)
