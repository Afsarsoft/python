# pyright: strict

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Reading json (JavaScript Object Notation) data
# Very common data format for storing information
# Being used for online APIs, configuration files, ...
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# It is very simillar to python dictionary
data: str = '''
{
    "name": "Sam",
    "age": 20,
    "salary": 5000
}
'''
print(data)
print(type(data))
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
