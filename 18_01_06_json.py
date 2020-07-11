# pyright: strict

import json

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Reading json data file
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
json_file: str = 'states.json'
with open(json_file, 'r') as f:
    data: dict = json.load(f)
    print(data)

for state in data['states']:
    print(state)

for state in data['states']:
    print(state['name'], state['abbreviation'])
