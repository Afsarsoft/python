# pyright: strict

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Tuples and Dicionaries
'''
name_counts: Dict[str, int] = {
    'Surush': 2,
    'Sam': 4,
}
'''

name_counts = {}
name_counts['Surush'] = 2
name_counts['Sam'] = 4
print(type(name_counts))

for (key, value) in name_counts.items():
    print(key, value)

print(name_counts)

name_counts_converted = ()
name_counts_converted = name_counts.items()
print(name_counts_converted)

print(type(name_counts_converted))
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
