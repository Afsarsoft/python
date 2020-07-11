# pyright: strict
from typing import Dict, Union

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
student: Dict[str, Union[str, int, list]] = {
    "name": "John Smith",
    "age": 30,
    'courses': ['Math', 'Physics']
}
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Let's add key value phone for our student dictionary
student['phone'] = '425-555-5555'
print(student)
print(student.get('phone'))

# Update our value for key value name
student['name'] = 'Jane'
print(student)
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Can have multiple actions with update statmnet:
# -Changing the values for name and age
# -Adding phone number
student: Dict[str, Union[str, int, list]] = {
    'name': 'John',
    'age': 25,
    'courses': ['Math', 'Physics']
}

student.update(
    {
        'name': 'Jane',
        'age': 30,
        'phone': '425-333-4444'
    }
)
print(student)
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Delete a key using del
student: Dict[str, Union[str, int, list]] = {
    'name': 'John',
    'age': 25,
    'courses': ['Math', 'Physics']
}

del student['age']
print(student)
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Delete a key using pop and keeping the value
student: Dict[str, Union[str, int, list]] = {
    'name': 'John',
    'age': 25,
    'courses': ['Math', 'Physics']
}

age = student.pop('age')
print(student)
print(age)
