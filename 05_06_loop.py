# pyright: strict
from typing import List

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Find sum of only multiples of 3
print(list(range(1, 10)))
some_range: List[int] = list(range(1, 10))

# For this we need to use % or modulo operator
total = 0
for number in some_range:
    if number % 3 == 0:
        total += number

message = f'Total of {some_range} for sum of only multiples of 3 is {total}!'
print(message)
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
