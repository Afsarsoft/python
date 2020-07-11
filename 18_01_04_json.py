# pyright: strict

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

print(f'See what data we have.')
for item in data['people']:
    print(item)

print(f'Remove the phone info.')
for item in data['people']:
    del item['phone']

print(f'See what data we have.')
for item in data['people']:
    print(item)

print(f'Dump to json string.')
new_data: str = json.dumps(data)
print(new_data)

#print(f'Indent and sort json str.')
#new_data: str = json.dumps(data, indent=2, sort_keys=True)
# print(new_data)
