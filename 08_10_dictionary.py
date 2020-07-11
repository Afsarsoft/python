# pyright: strict
from typing import List

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Count Names
# For a new name, add it to dictionary
# for existing name, add the count of name
name: str = ''
name_counts: dict = {}
names: List[str] = ['Surush', 'Tom', 'Steve', 'Surush', 'Jim', 'Mary', 'Steve']
for name in names:
    if name not in name_counts:
        name_counts[name] = 1
        print(name_counts)
    else:
        name_counts[name] += 1
        print(name_counts)

print(name_counts)

# Making above simpler
name: str = ''
name_counts: dict = {}
names: List[str] = ['Surush', 'Tom', 'Steve', 'Surush', 'Jim', 'Mary', 'Steve']
for name in names:
    name_counts[name] = name_counts.get(name, 0) + 1
    print(name_counts)

print('completed!', 'Counts = ', name_counts)
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
