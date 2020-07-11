# pyright: strict
from typing import List

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Find the largest value
numbers: List[int] = [33, 41, 12, 3, 74, 15, 10]
largest: int = numbers[0]

print(f'Before -> {largest}')

for number in numbers:
    if number > largest:
        largest = number
    print(largest, number)

print(f'After -> {largest}')
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Find the largest value, easy way
largest: int = max(numbers)

print(f'largest -> {largest}')
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
