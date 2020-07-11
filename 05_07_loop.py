# pyright: strict
from typing import List

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Add only positive numbers
nums: List[int] = [5, -7, 4, -2, 1, -2, -3, 5, -1]
total: int = 0

for num in nums:
    if num > 0:
        total += num

print(f'Total of the {nums} for only positive numbers = {total}')
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Add only negative numbers
total: int = 0

for num in nums:
    if num <= 0:
        total += num

print(f'Total of the {nums} for only negative numbers = {total}')
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
