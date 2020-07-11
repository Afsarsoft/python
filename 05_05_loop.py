# pyright: strict
from typing import List

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Create range of numbers 1-5 not including 5
# Basically, only 1, 2, 3, 4
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
num: int = 0
total: int = 0

some_range: List[int] = list(range(1, 5))
print(f'some_range -> {some_range}')

for num in some_range:
    total += num

message = f'Total of {some_range} is {total}!'
print(message)
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Total of range of numbers 1-5 not including 5, easy
total = sum(some_range)

message = f'Total of {some_range} is {total}!'
print(message)
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
