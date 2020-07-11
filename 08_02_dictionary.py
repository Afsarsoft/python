# pyright: strict
from typing import Dict, Union

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
customer: Dict[str, Union[str, int, bool]] = {
    "name": "John Smith",
    "age": 30,
    "is_verified": True,
}
print(customer["name"])
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# Let's get value of one key
print(customer['name'])

# Let's get the age
print(customer['age'])

# Key values can be any data types, in above examples are alll string
# How about accessing a key which no exist? we get an error
# print(customer['phone'])

# We better to use get methon dictionary to avoid getting an error
print(customer.get('phone'))  # getting None instead of an error
print(customer.get('name'))

# We can have default value if not found
print(customer.get('phone', 'phone, Not Found!'))
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
