# pyright: strict
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# We can put a tuple on the left-hand side of an assignment statement
# Note: you can return a tuple from function
from typing import Tuple

(x, y) = (4, 'fred')
print(x)
print(y)

tuple_2: Tuple[int, str] = (x, y)
print(tuple_2)

(a, b) = (99, 98)
print(a)
print(b)

tuple_3: Tuple[int, int] = (a, b)
print(tuple_3)
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
