# pyright: strict
# Work on this
# https://3.python-requests.org/
# https://www.youtube.com/watch?v=tb8gHvYlCFs


'''
# ++++++++++++++++++++++++++
# Reading json data from public API
# ++++++++++++++++++++++++++
import json
from urllib.request import urlopen

json_url: str = 'https://api.github.com/users/mralexgray/repos'

with urlopen(json_url) as response:
    source = response.read()

# print(source)
print(type(source))

decoded_data = source.decode('utf-8')
print(type(decoded_data))
# print(decoded_data)

data = json.loads(decoded_data)

# cleanup to see look better
print(json.dumps(data, indent=4))

print(f'Name: {data["full_name"]}')
'''
'''
for item in data['full_name']:
    print(item)
'''
