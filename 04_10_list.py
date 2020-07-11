# pyright: strict
from typing import List

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Swapping items in list, swapping first one with other one
stuff2: List[str] = ["banana", "apple", "microsoft"]

temp = stuff2[0]
stuff2[0] = stuff2[2]
stuff2[2] = temp
print(stuff2)

# another approach!
stuff3: List[str] = ["banana", "apple", "microsoft"]
stuff3[0], stuff3[2] = stuff3[2], stuff3[0]
print(stuff3)
