# Here we will round up all of the string methods in one place:

# here we have a long string of poems, authors and dates, separated by colons
highlighted_poems = "Afterimages:Audre Lorde:1997,  The Shadow:William Carlos Williams:1915, Ecstasy:Gabriela Mistral:1925,   Georgia Dusk:Jean Toomer:1923,   Parting Before Daybreak:An Qi:2014, The Untold Want:Walt Whitman:1871, Mr. Grumpledump's Song:Shel Silverstein:2004, Angel Sound Mexico City:Carmen Boullosa:2013, In Love:Kamala Suraiyya:1965, Dream Variations:Langston Hughes:1994, Dreamwood:Adrienne Rich:1987"

print(highlighted_poems)

highlighted_poems_list = highlighted_poems.split(',')
# here, we create a list, where each element has the format poem:author:date

print(highlighted_poems_list)

highlighted_poems_stripped = []
# instantiate a new list

for element in highlighted_poems_list:
    stripped_element = element.strip()
    highlighted_poems_stripped.append(stripped_element)
# this loop strips any errant whitespace from each element

print(highlighted_poems_stripped)

highlighted_poems_details = []
# instantiate another new list

for element in highlighted_poems_stripped:
    details_list = element.split(':')
    highlighted_poems_details.append(details_list)
# this loop splits each element around the colon and appends them to the new list
# this creates a list of lists

print(highlighted_poems_details)

titles = []
poets = []
dates = []
# instantiate three new lists

for element in highlighted_poems_details:
    titles.append(element[0])
    poets.append(element[1])
    dates.append(element[2])
# this loop appends the elements of each sub-list in the list to one of the three lists above

print(titles)
print(poets)
print(dates)

for element in range(len(titles) - 1):
    string = "The poem {title} was published by {poet} in {date}".format(title=titles[element], poet=poets[element], date=dates[element])
    print(string)
# This uses format() to print the string
# we use len(titles) - 1 to get the length of the lists so that we loop over the lists the exact number of times we need
