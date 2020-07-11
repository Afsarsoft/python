# pyright: strict
from typing import List

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Display emojis
message: str = str(input(">"))
words: List[str] = message.split(' ')

emojis: dict = {
    ":)": "😊",
    ":(": "😂"
}

output = ""
for word in words:
    output += emojis.get(word, word) + " "

print(output)
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Tuples and Dicionaries
name_counts: dict = {}
name_counts['Surush'] = 2
name_counts['Sam'] = 4
print(type(name_counts))

for (key, value) in name_counts.items():
    print(key, value)

print(name_counts)

name_counts_converted: tuple = ()
name_counts_converted = name_counts.items()
print(name_counts_converted)

print(type(name_counts_converted))


d = {}
d['Surush'] = 2
d['Sam'] = 4
for (k, v) in d.items():
    print(k, v)

t = ()
t = d.items()
print(type(t))
print(t)
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
