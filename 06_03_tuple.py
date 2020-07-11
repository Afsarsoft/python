# pyright: strict
from typing import List, Tuple

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# You can have tuples inside list to not be changed
coordinates: List[Tuple[int, int]] = [(4, 5), (6, 7), (80, 34)]
print(coordinates)
print(coordinates[1])

for item in coordinates:
    print(item)
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Tuples are comparable, comprasion is from left to right
#from typing import Tuple
tuple_01: Tuple[int, ...] = (0, 1, 2)
tuple_02: Tuple[int, ...] = (5, 1, 2)
print(tuple_01 < tuple_02)

tuple_03: Tuple[int, ...] = (0, 1, 20000)
tuple_04: Tuple[int, ...] = (0, 3, 4)
print(tuple_03 < tuple_04)

tuple_05: Tuple[str, ...] = ('Jones', 'Sally')
tuple_06: Tuple[str, ...] = ('Jones', 'Sam')
print(tuple_05 < tuple_06)

tuple_07: Tuple[str, ...] = ('Jones', 'Sally')
tuple_08: Tuple[str, ...] = ('Adams', 'Sam')
print(tuple_07 < tuple_08)
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
