# pyright: strict
from typing import Dict

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# get lists of keys and values
name_counts: Dict[str, int] = {
    'chuck': 1,
    'fred': 42,
    'jan': 100
}

# get keys
print(list(name_counts))

# get keys
print(name_counts.keys())

# get values
print(name_counts.values())

# get keys and values
print(name_counts.items())

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Loops in dictionaries
for key in name_counts:
    print(key, name_counts[key])


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Sorted dictionary items
letter_counts: Dict[str, int] = {
    'c': 10,
    'b': 1,
    'a': 22
}
letter_counts.items()
sorted(letter_counts.items())

for (k, v) in sorted(letter_counts.items()):
    print(k, v)

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# sort by values instead of keys
letter_counts: Dict[str, int] = {
    'c': 10,
    'b': 1,
    'a': 22
}

sorted_list: list = []

for k, v in letter_counts.items():
    sorted_list.append((v, k))

print(sorted_list)

sorted_list = sorted(sorted_list, reverse=True)
print(sorted_list)
