# pyright: strict
from typing import List

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
nums: List[int] = [1, 2, 3, 4, 5]
for num in nums:
    print(num)
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Break compltely breaks out and exit the loop
for num in nums:
    if num == 3:
        print(f'Found {num}!')
        break
    print(num)
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Continue ignores the condition and continue the loop
for num in nums:
    if num == 3:
        print(f'Found {num}!')
        continue
    print(num)
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
