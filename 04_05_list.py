# pyright: strict
from typing import List

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# To remove one element from the end of the list
friends: List[str] = ["Surush", "Jack", "Mary", "Sam", "Ana", "Sonia"]
print(friends)
friends.pop()
print(friends)

# Notice that pop returns the valued that removed
popped = friends.pop()
print(popped)
print(friends)

# To search for a value or element exist in the list
print(friends.index("Mary"))  # Return the position of element if exists
# print(friends.index("Steve"))  # Retrun error if element not exists

# Or, from typing import List
print('Surush' in friends)  # Retrurn True if exist
print('Steve' in friends)  # Retrurn False if not exist

# To have string with embeded character use join
print('Friends ->', friends)
friends_str = '|'.join(friends)
print('Friends ->', friends)  # no impact to friends
print('Friends_str ->', friends_str)

# We can get back to original list using split
new_friends = friends_str.split('|')

print('Friends ->', friends)
print('new_friends ->', new_friends)

print('Friends ->', friends)
friends_str = ' - '.join(friends)
print('Friends ->', friends)  # no impact to friends
print('Friends_str ->', friends_str)
