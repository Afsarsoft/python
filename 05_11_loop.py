# pyright: strict
from typing import List

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Nested loops (Loop within a loop)
nums: List[int] = [1, 2, 3, 4, 5]
letters: str = 'abc'

for num in nums:
    for letter in letters:
        print(f'Number = {num}, Letter = {letter}')
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Another example
x: int = 0
y: int = 0
for x in range(4):
    for y in range(3):
        print(f'({x}, {y})')
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
