# pyright: strict

import json

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Reading json data file
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
json_file: str = 'test1.json'
with open(json_file) as f:
    data: dict = json.load(f)
    print(data)
