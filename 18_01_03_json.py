# pyright: strict

# Table for json object and types conversion
# https://docs.python.org/3/library/json.html#py-to-json-table

import json

people_string: str = '''
{
    "people": [
        {
            "name": "John Smith",
            "phone": "615-555-7164",
             "has_license": false
        },
        {
            "name": "Jane Doe",
            "phone": "560-555-5153",
             "has_license": true
        }
    ]
}
'''
data: dict = json.loads(people_string)

print(type(data['people']))

for item in data['people']:
    print(item)

for item in data['people']:
    print(item['name'])
