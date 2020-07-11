# pyright: strict
from typing import List

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Finding the average
count: int = 0
total: int = 0
numbers: List[int] = [9, 41, 12, 3, 74, 15]

for number in numbers:
    count += 1
    total += number
    print(f'Count = {count}, Number = {number}, Total = {total}')

print(f'In {count} numbers, Total = {total}, Average = {total/count}')

# Finding the average, easy
total: int = sum(numbers)
count: int = len(numbers)
print(f'In {count} numbers, Total = {total}, Average = {total/count}')
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
