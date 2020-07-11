# pyright: strict
from typing import List

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Object Identity:  is
a: List[int] = [1, 2, 3]
b: List[int] = [1, 2, 3]

print(a == b)  # as we expected the result is True

# the result is False, because they are 2 different object in memory
print(a is b)

# We can see thier location in memory as follow:
print(id(a))
print(id(b))
print(a is b)

# or saying like as follow
print(id(a) == id(b))
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
