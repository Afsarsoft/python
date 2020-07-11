# pyright: strict

from typing import List

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
friends: List[str] = []   # To create an empty set, no need to have this line
friends: List[str] = ["Surush", "Jack", "Mary", "Sam", "Ana", "Sonia"]

for friend in friends:
    print(f'My friend is {friend}')
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# to see index values as well in result
for index, friend in enumerate(friends):
    print(f'Friends values using enumerate function-> {index} - {friend}')
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# We can have start value as well
for index, friend in enumerate(friends, start=1):
    print(
        f'Friends values using enumerate function starting from 1-> {index} - {friend}')
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
