# The finally clause can be used in the try / except / else sequence
# the finally clause is unique in that it can always be used - it doesn't to come after an except or else clause
# this is useful for guaranteeing that some code is run, no matter if an exception is raised
# this example considers loading a database of instruments

import database
# we import the instruments dictionary and database methods from the database.py file

instrument = 'Kora'
# instrument = 'Synthesizer'
database.connect_to_database()

try:
    database.display_instrument_info(instrument)
    # tries to load the information

except KeyError:
    print('Oh no! This instrument does not exist.')
    # triggers if instrument is not valid

else:
    print(instrument)
    # works if instrument is valid

finally:
    database.disconnect_from_database()
# Regardless of what happens, this clause will always trigger, as we want to log off
