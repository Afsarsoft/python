# pyright: strict

import json

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Reading json data file
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
json_file: str = 'states.json'
json_dump_file: str = 'states_dump.json'
json_dump_file_format: str = 'states_dump_format.json'

print(f'Open json file {json_file}.')
with open(json_file, 'r') as f:
    data: dict = json.load(f)
    print(data)

print(f'Remove the area code.')
for state in data['states']:
    del state['area_codes']

print(f'Dump to new json file {json_dump_file}.')
with open(json_dump_file, 'w') as f:
    json.dump(data, f)

print(f'Dump to new json file formatted {json_dump_file_format}.')
with open(json_dump_file_format, 'w') as f:
    json.dump(data, f, indent=2)
