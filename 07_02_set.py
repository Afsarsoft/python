# pyright: strict
from typing import Set

# +++++++++++++++++++++++++++++++++++++++++++++++++++++
# sets are great for value sharing check
#from typing import Set
courses1: Set[str] = {'History', 'Math', 'Physics', 'Chemistry'}
courses2: Set[str] = {'History', 'Math', 'Sport', 'Art', 'Physics'}

# Checking for common or shared values
print(courses1.intersection(courses2))

# Checking for not common or not shared values
print(courses1.difference(courses2))
print(courses2.difference(courses1))

# to combine or add both sets which removes duplicates
print(courses1.union(courses2))
# +++++++++++++++++++++++++++++++++++++++++++++++++++++
