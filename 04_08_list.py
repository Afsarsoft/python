# pyright: strict
from typing import List, Union

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Can mix and match data types
stuff: List[Union[str, int, bool]] = ["Surush", "Mary", "Table",
                                      True, False, "Sam", 99, 20, "TV", "Radio"]
print(stuff)
