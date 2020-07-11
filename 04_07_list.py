# pyright: strict
from typing import List

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# copy, 1
friends: List[str] = ["Surush", "Jack", "Mary", "Sam", "Ana", "Sonia"]
print(friends)
friends1 = friends.copy()
print(friends1)

# copy, 1
friends: List[str] = ["Surush", "Jack", "Mary", "Sam", "Ana", "Sonia"]
print(friends)
friends1 = friends
print(friends1)
