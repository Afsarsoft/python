# pyright: strict

from typing import List, Tuple, Set

# Importing our own py library
# Here the py file is in same folder
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#from my_module import *
#from my_module import find_index, test
#from my_module import find_index
#import my_module
import my_module as mm

courses1: Tuple[str, ...] = ('History', 'Math', 'Physics')
index = mm.find_index(courses1, 'Math')
print(index)

courses2: List[str] = ['History', 'Math', 'Physics']
index = mm.find_index(courses2, 'Physics')
print(index)

courses3: Set[str] = {'History', 'Math', 'Physics'}
index = mm.find_index(courses3, 'History')
print(index)

message: str = 'History'
index = mm.find_index(message, 'r')
print(index)

message: str = 'History4'
index = mm.find_index(message, '4')
print(index)

# Not abl to fins this
message: str = 'HistoryIsSoCocool'
index = mm.find_index(message, 'Is')
print(index)

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
