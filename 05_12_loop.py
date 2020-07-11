# pyright: strict
from typing import List

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Lets's draw a following F shape below.
# XXXXX
# XX
# XXXXX
# XX
# XX

# Easy way
count: int = 0
numbers: List[int] = [5, 2, 5, 2, 2]

for count in numbers:
    print('x' * count)

# Nested loop way
count1: int = 0
count2: int = 0
output: str = ''
numbers: List[int] = [5, 2, 5, 2, 2]

for count1 in numbers:
    output = ''
    for count2 in range(count1):
        output += 'X'
    print(output)
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
