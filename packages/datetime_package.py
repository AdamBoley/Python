# datetime is a standard Python package
# we import it like so:
from datetime import datetime

# If we only use the following:
# import datetime
# Then we need to use datetime.datetime.now() below
# also, don't names files after packages - this will cause errors

# the now() method grabs the exact time down to the millisecond when the program is run
current_time = datetime.now()

print(current_time)

# We can also use datetime to create date and time objects:
birthday = datetime(1992, 10, 7, 4, 20)

# When we create a datetime variable, we must pass in a year, a month and day
# we can then optionally pass in hours, minutes, seconds, milliseconds and a timezone, in that order
# in the birthday object above, we define my birthday and the time - 4:20 in the morning, on October 7th, 1992
# the datetime method creates a Python dictionary, which can be accessed:
print(birthday.year)
print(birthday.month)
print(birthday.day)
print(birthday.hour)
print(birthday.minute)

# We can get a little more information:
print(birthday.weekday())
# weekday is a number between 0 and 6, 0 being Monday and 6 being Sunday
# This outputs 2, meaning Wednesday

# This should highlight some differences - months and days are 1-indexed, January is represented by 1
# weekday is 0-indexed - Monday is represented with 0

# We can get time differences using the subtraction operation:
print(datetime(2023, 1, 1) - datetime(2022, 1, 1))
# outputs 365 days
# if done in the Python terminal, this outputs datetime.timedelta(days=365)
# timedelta is a time difference

# We can also create a datetime object from a string
# This requires the strptime function and a special syntax:

parsed_date = datetime.strptime('Oct 07, 1992', '%b %d, %Y')

# strptime means 'string parsed time'
# Note that we pass in 2 string arguments - the date and a bunch of % signs with letters
# the date is the date that we want to parse
# the second string is format of the date
# In this case, %b means the abbreviated Month - Oct, Jan, Aug
# %d means the day as 2 digits - 07, 15, 31
# %Y means a 4 digit year, including millenium and century - 2017, 1995, 0982, etc
# a full list is here - https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes
# be sure to include any formatting characters such as colons and commas
print(parsed_date.day)

# strftime is the reverse of strptime
date_string = datetime.strftime(datetime.now(), '%b %d, %Y')
print(date_string)
# Note that we use the same syntax in the second string to specify the format
