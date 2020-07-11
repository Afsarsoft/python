# pyright: strict

# tuples are similar to the lists
# The main difference is that
# we cannot modify the tuples
# In programming it called immutable
# lists are mutable and tuples are immutable
from typing import Tuple, Any

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# t: tuple = tuple()   # To create an empty tuple
# t: tuple[Any]
# t: tuple = ()        # more common way to create an empty tuple 1
# t = ()               # more common way to create an empty tuple 2
# print(t)
# type(t)
# dir(t)
# help(tuple)
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# If we know that valuse are not going to change,
# We better use tuples for better performance and security
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
numbers: Tuple[int, ...] = (1, 2, 5, 7, 9)

# Bad practice
stuff: Tuple[Any, ...] = (1, 2, 'something', 5, True, 7, 9)

courses: Tuple[str, ...] = ('History', 'Math', 'Physics',
                            'Algebra', 'Art', 'Dance')

print(f'first info is {courses[0]}')
print(f'Third info is {courses[2]}')
print(f'Forth info is {courses[3]}')
print(f'Fifth info is {courses[4]}')

# Immutable Example
# We get error in here, since no support for it
#cources[4] = 'Chemesity'

# copying
courses_new: Tuple[str, ...] = courses

print(f'cources -> {courses}')
print(f'cources_new -> {courses_new}')

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# For somthing only for access and loop through use tuples
print(courses.count('History'))
print(courses.index('Physics'))

for course in courses:
    print(course)
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
