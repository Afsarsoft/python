# pyright: strict
from typing import Dict

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Get digits and translate to letters
phone: str = str(input("Phone:"))
digits_mapping: Dict[str, str] = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine",
    "0": "Zero"
}

output: str = ""
number: str = ""
for number in phone:
    output += digits_mapping.get(number, "!") + " "

print(output)
