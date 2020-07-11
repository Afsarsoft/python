# pyright: strict
from typing import Union

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# *args = use when not sure how many arguments might be
#         passed to the function, capture as a tuple
# **kwargs = same as args but captures as dictionary
# The names *args and **kwargs are only by convention and there's no hard requirement to use them.
# Can use both in the same function but *args must occur before **kwargs.

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


def print_everything1(*args: str)-> None:
    for stuff in (args):
        print(f'passing value -> {stuff}')


print_everything1('apple', 'bnana', 'cabbage')
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


def print_everything2(*args: Union[str, int, float, bool])-> None:
    for count, stuff in enumerate(args):
        print(f'{count}- {stuff}')


print_everything2('apple', 'bnana', 'cabbage', True, False, 3, 3.5)
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


def get_everything(*args: str) -> str:
    result: str = ''

    # capture as a tuple
    # print(type(args))

    for stuff in (args):
        result += stuff + ' '
    return result


message: str = get_everything(
    'apple', 'bnana', 'cabbage') + '-> get_everything'
print(message)
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
