# pyright: strict
from typing import Set

# sets are values which are un ordered and have no duplicates
# To create a empt sets use set()
# '''
# +++++++++++++++++++++++++++++++++++++++++++++++++++++
# '''
# s: Set[str]   # To create an empty set
# s: set = set()
# print(type(s))
# print(s)
# dir(s)
# help(set)
# +++++++++++++++++++++++++++++++++++++++++++++++++++++

# +++++++++++++++++++++++++++++++++++++++++++++++++++++
# We use sets to check if a value exist or remove duplicate values
# Because sets are optimized for checking the values and duplicates
courses: Set[str] = {'History', 'Math', 'Physics', 'Math'}

# As you see duplicate Math not showing
print(courses)
# +++++++++++++++++++++++++++++++++++++++++++++++++++++

# Also, it is very fast to chech for a value
print('Physics' in courses)
# +++++++++++++++++++++++++++++++++++++++++++++++++++++
