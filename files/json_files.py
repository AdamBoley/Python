# Python can also be used to read JSON files
# JSON stands for JavaScript Object Notation

# JSON files can be opened in the same way as TXT and CSV files:

import json

with open('message.json') as message_json:
    message = json.load(message_json)

print(message['text'])
# prints the value of the "text" key, which is "Now that's JSON"

# Naturally, we can write to JSON files as well:

data_payload = [
  {'interesting message': 'What is JSON? A web application\'s little pile of secrets.',
   'follow up': 'But enough talk!'}
]

with open('data.json', 'w') as data_json:
    json.dump(data_payload, data_json)

# This doesn't need a data.json file to exist first
# When the code is run, a file is created holding the dumped information


