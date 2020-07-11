# pyright: strict
from typing import Dict, Union

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# To see how many keys we have in our dictionary
student: Dict[str, Union[str, int, list]] = {
    'name': 'John',
    'age': 25,
    'courses': ['Math', 'Physics']
}
print(len(student))

# To see the keys of our dictionary
print(student.keys())

# To see the values of our dictionary
print(student.values())

# To see the keys and values of pir dictionary
print(student.items())

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Looping through our keys
for key in student:
    print(key)

# For keys and values , use items method
for key, value in student.items():
    print(key, value)
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
