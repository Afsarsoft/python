# pyright: strict
from typing import List, Dict, Union

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# *args = use when not sure how many arguments might be
#         passed to the function, capture as a tuple
# **kwargs = same as args but captures as dictionary
# The names *args and **kwargs are only by convention and there's no hard requirement to use them.
# Can use both in the same function but *args must occur before **kwargs.
# https://stackoverflow.com/questions/3394835/use-of-args-and-kwargs
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


def student_info1(*args: str, **kwargs: Union[str, int]):
    print(args)
    print(kwargs)


# Use * and ** when calling a function
courses: List[str] = ['Math', 'Art']
info: Dict[str, Union[str, int]] = {'name': 'John', 'age': 22}

student_info1(*courses, **info)

# +++++++++++++++++++++++++++++++++++++++++++++++++++++


def student_info2(**kwargs: Union[str, int]):
    print(kwargs)


info: Dict[str, Union[str, int]] = {'name': 'John', 'age': 22}
student_info2(**info)


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


def print_stuff(**kwargs: Union[str, str]):
    for key, value in kwargs.items():
        print(f'{key} = {value}')


info1: Dict[str, Union[str, str]] = {'apple': 'fruit', 'cabbage': 'vegetable'}
info2: Dict[str, Union[str, str]] = {'orange': 'fruit', 'parsly': 'vegetable'}
info3: Dict[str, Union[str, str]] = {'banana': 'fruit', 'potato': 'vegetable'}

print_stuff(**info1)
print_stuff(**info2)
print_stuff(**info3)
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
