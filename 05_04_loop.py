# pyright: strict
from typing import List

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Add total of a list
prices: List[int] = [20, 10, 5]
total: int = 0

for price in prices:
    total += price

message = f'Total of {prices} is {total}!'
print(message)
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Add total of a list, easy
total: int = sum(prices)

message = f'Total of {prices} is {total}!'
print(message)
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
