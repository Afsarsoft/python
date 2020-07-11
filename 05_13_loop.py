# pyright: strict
from typing import List

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# 2D list, just list inside list
number_grid: List[list] = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

# gives us 1
print(number_grid[0][0])

# gives us 5
print(number_grid[1][1])

# to acess to the rows
for row in number_grid:
    print(row)

# 2D list
# to acess everything, need to have nested loops
for row in number_grid:
    for col in row:
        print(col)
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
