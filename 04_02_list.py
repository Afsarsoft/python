# pyright: strict
from typing import List

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
friends: List[str] = ["Surush", "Jack", "Mary", "Sam", "Ana", "Sonia"]
print(f'List of friends are {friends}')
print(f'My first friend is {friends[0]}')
print(f'My third friend is {friends[2]}')
print(type(friends))
dir(friends)
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
