# pyright: strict

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Reading json (JavaScript Object Notation) data
# Very common data format for storing information
# Being used for online APIs, configuration files, ...
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# It is very simillar to python dictionary
import json
data: str = '''
{
    "name": "Sam",
    "age": 20,
    "salary": 5000
}
'''
print(type(data))

info: dict = json.loads(data)
print(info)
print(type(info))

print(f'Name: {info["name"]}')
print(f'Age: {info["age"]}')
print(f'Salary: {info["salary"]}')
