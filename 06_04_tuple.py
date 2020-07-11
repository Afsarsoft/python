# pyright: strict
from typing import List, Tuple, Any

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Tuples are comparable, comprasion is from left to right
# x: List[Union[int, str]] = [3, 5, "test", "fun"]
# https://mypy.readthedocs.io/en/latest/cheat_sheet_py3.html
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

stuff1: List[Tuple[int, int, int]] = [
    (0, 1, 2), (5, 1, 2),
    (0, 4, 20000), (0, 3, 4)
]

target: int = len(stuff1)
count: int = 0

while count <= target - 1:
    if stuff1[count] < stuff1[count+1]:
        print(f'{stuff1[count]} < {stuff1[count+1]}')
    elif stuff1[count] > stuff1[count+1]:
        print(f'{stuff1[count]} > {stuff1[count+1]}')
    elif stuff1[count] == stuff1[count+1]:
        print(f'{stuff1[count]} = {stuff1[count+1]}')
    else:
        print('Something went wrong!')
    count += 2

print(target)
print(count)
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

stuff2: List[Tuple[str, str]] = [
    ('Jones', 'Sally'), ('Jones', 'Sam'),
    ('Jones', 'Sally'), ('Adams', 'Sam'),
    ('Surush', 'Sally'), ('Jack', 'Alice'),
    ('Aiden', 'Mark'), ('Hellen', 'Steve')
]

target: int = len(stuff2)
count: int = 0

while count <= target - 1:
    if stuff2[count] < stuff2[count+1]:
        print(f'{stuff2[count]} < {stuff2[count+1]}')
    elif stuff2[count] > stuff2[count+1]:
        print(f'{stuff2[count]} > {stuff2[count+1]}')
    elif stuff2[count] == stuff2[count+1]:
        print(f'{stuff2[count]} = {stuff2[count+1]}')
    else:
        print('Something went wrong!')
    count += 2

print(target)
print(count)

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Don't combine disparate types in a single list.
# Doing so is not very type friendly.
# Most typed languages wouldn't even allow you to do this.
# If you require the more dynamic behavior,
# specify a type of 'List[Any]' for your list.
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
stuff3: List[Any] = [
    (0, 1, 2), (5, 1, 2),
    (0, 4, 20000), (0, 3, 4),
    ('Jones', 'Sally'), ('Jones', 'Sam'),
    ('Jones', 'Sally'), ('Adams', 'Sam'),
]

target: int = len(stuff3)
count: int = 0

while count <= target - 1:
    if stuff3[count] < stuff3[count+1]:
        print(f'{stuff3[count]} < {stuff3[count+1]}')
    elif stuff3[count] > stuff3[count+1]:
        print(f'{stuff3[count]} > {stuff3[count+1]}')
    elif stuff3[count] == stuff3[count+1]:
        print(f'{stuff3[count]} = {stuff3[count+1]}')
    else:
        print('Something went wrong!')
    count += 2

print(target)
print(count)
