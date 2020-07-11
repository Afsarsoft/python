# pyright: strict
from typing import Dict

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Dictionaries allows us to work with key value pairs
# It is like lookup table
# In order languages called them hash maps or associated of arrays
# Key is key identifier and the value is the data
# Like physical dictionary
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# consider a student
# customer: dict = {}  # more common approach
# print(customer)
# print(type(customer))
# or as follow
# student: dict = dict()
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

month_conversion1: Dict[str, str] = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
}
print(month_conversion1)
type(month_conversion1)
# dir(month_conversion1)
# help(dict())

# They are different ways to acces the values
print(month_conversion1["Nov"])
print(month_conversion1["Mar"])
# print(month_conversion1["Vul"])  # here we are gettign error because key not found


# the get approach is better way since we can assign default values if key not found
# Also, we do not get an error
print(month_conversion1.get("Dec", "Not a valid key!"))
print(month_conversion1.get("Vul", "Not a vaild key!"))
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Different approach
month_conversion2: Dict[int, str] = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December",
}

print(month_conversion2[10])
print(month_conversion2[3])
# print(month_conversion2[22)

print(month_conversion2.get(11, "Not a valid key!"))
print(month_conversion2.get(22, "Not a vaild key!"))
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
