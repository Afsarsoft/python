# pyright: strict
from typing import List

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Find the smallest value
numbers: List[int] = [33, 41, 12, 3, 74, 15, 10]
smallest: int = numbers[0]

print(f'Before -> {smallest}')

for number in numbers:
    if number < smallest:
        smallest = number
    print(smallest, number)

print(f'After -> {smallest}')
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Find the smallest value, easy way
largest: int = min(numbers)

print(f'After -> {smallest}')
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
