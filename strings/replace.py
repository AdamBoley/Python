# replace() is used to replace one substring with another
# it takes 2 parameters - the first is the substring you want to be replaced, and the second is the substring you want to insert

# This means that replace() can be used to fix spelling mistakes

# Below we have a biography of Nathan Pinchback Toomer, where his last name is spelled incorrectly
# we can use replace() to fix this:

toomer_bio = \
"""
Nathan Pinchback Tomer, who adopted the name Jean Tomer early in his literary
 career, was born in Washington, D.C. in 1894. Jean is the son of Nathan Tomer 
 was a mixed-race freedman, born into slavery in 1839 in Chatham County, 
 North Carolina. Jean Tomer is most well known for his first book Cane, 
 which vividly portrays the life of African-Americans in southern farmlands.
"""

toomer_bio_fixed = toomer_bio.replace('Tomer', 'Toomer')
# here we replace all instances of Tomer with Toomer

print(toomer_bio_fixed)
