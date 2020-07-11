# pyright: strict
from typing import Dict, Union

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
student: Dict[str, Union[str, int, list]] = {
    "name": "John Smith",
    "age": 30,
    'courses': ['Math', 'Physics']
}
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Let's get value of one key, name of the student
print(student['name'])

# Let's get the courses
print(student['courses'])

# Key values can be any data types, in above examples are alll string
# How about accessing a key which no exist? we get an error
# print(student['phone'])

# We better to use get methon dictionary to avoid getting an error
print(student.get('phone'))  # getting None instead of an error
print(student.get('name'))

# We can have default value if not found
print(student.get('phone', 'phone, Not Found!'))
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
