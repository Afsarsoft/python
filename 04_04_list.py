# pyright: strict
from typing import List

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Adding individual elements to the end
friends: List[str] = ["Surush", "Jack", "Mary", "Sam", "Ana", "Sonia"]
print(friends)
friends.append("John")
print(friends)

# Adding individual elements in middle
friends.insert(1, "Kelly")
print(friends)

# Remove an lelment
friends.remove("Sam")
print(friends)

# To remove everything from the list
friends.clear()
print(friends)
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
