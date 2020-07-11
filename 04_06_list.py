# pyright: strict
from typing import List

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# To count number of values
friends: List[str] = [
    "Surush", "Jack",
    "Mary", "Mary", "Sam",
    "Ana", "Sonia"
]
print(friends.count("Mary"))
print(friends.count("Jack"))

# to sort the list
print(f'Original {friends}')
friends.sort()  # Asending order
print(f'Asending order {friends}')
friends.sort(reverse=True)  # Desending order
print(f'Desending order easier {friends}')

# To not effect the original list in sorting
friends: List[str] = ["Surush", "Jack", "Mary", "Sam", "Ana", "Sonia"]
print(f'Existing list {friends}')
sorted_friends = sorted(friends)
print(f'Desending order on new list {sorted_friends}')

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# to reverse
# from typing import List
friends: List[str] = ["Surush", "Jack", "Mary", "Sam", "Ana", "Sonia"]
print(friends)
friends.reverse()
print(friends)
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
