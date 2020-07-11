# pyright: strict
from typing import List

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Removing duplicates
numbers: List[int] = [2, 2, 4, 6, 3, 4, 6, 1]
uniques: List[int] = []

print(numbers)

for number in numbers:
    if number not in uniques:
        uniques.append(number)

print(uniques)
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
