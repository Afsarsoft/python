# pyright: strict
from typing import List, Union

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# To append another list
numbers1: List[Union[int, str]] = [20, 40, 100, 80, 12, 90, 5, -1, 30, -99]
friends1: List[Union[int, str]] = [
    "Surush", "Jack", "Mary", "Sam", "Ana", "Sonia"]

numbers_friends1: List[Union[int, str]] = numbers1 + friends1
print(numbers_friends1)
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# To append another list, old style
numbers2: list = [20, 40, 100, 80, 12, 90, 5, -1, 30, -99]
friends2: list = ["Surush", "Jack", "Mary", "Sam", "Ana", "Sonia"]

numbers_friends2 = friends2.extend(numbers2)
print(friends2)
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
