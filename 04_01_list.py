# pyright: strict

# List like array in other languages
# List and Tuples helps us to work with sequential data
# Sets are unorder collections of values with no duplicates
# '''
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
from typing import List

# l: List = list()  # To create an empty list
l: list = []      # more common way to create an empty list
# l: List[str] = []  # No empty list from str type, better way
print(l)
type(l)
dir(l)
help(list)
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# For collections, the name of the type is capitalized, and the
# name of the type inside the collection is in brackets
numbers: List[int] = [20, 40, 100, 80, 12, 90, 5, -1, 30, -99]
print(f"Len of numbers are {len(numbers)}")
print(f"List of numbers are {numbers}")
print(f"My first number is {numbers[0]}")
print(f"My third number is {numbers[2]}")

# We can use the negative numbers to go from the last
# Good approach to get always the last item to use -1
print(f"My last number is {numbers[-1]}")

# To get the range of items, starting not including
print(f'From first and not including third {numbers[0:2]}')
print(f"From second and the end {numbers[2:]}")

type(numbers)
# dir(numbers)
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
