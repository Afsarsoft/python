# pyright: strict
from typing import ClassVar


#  ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#  Inheritance
#  ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Inheritance allows us to inherit attributes and methods from a parent class
# We can create sub classes and get all the fuctionality of our parent class
# and we can overwrite or add new functionality without effecting our parent class.
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
class Employee:

    raise_amt: ClassVar[float] = 1.04  # %4

    def __init__(self, first: str, last: str, pay: int) -> None:
        self.first: str = first
        self.last: str = last
        self.pay: int = pay
        self.email: str = f'{first}.{last}@company.com'

    def fullname(self) -> str:
        return f'{self.first} {self.last}'

    def apply_raise(self) -> None:
        self.pay = int(self.pay * self.raise_amt)


# Now, we want our developers get %10 raise
class Developer(Employee):
    # overwriting the parent
    raise_amt: ClassVar[float] = 1.10


dev_1: Developer = Developer('Surush', 'Cyrus', 50000)
dev_2: Developer = Developer('Steve', 'Brown', 60000)

print(f'dev_1 --> First Name: {dev_1.first}, Pay: {dev_1.pay}')
dev_1.apply_raise()
print(f'dev_1 --> First Name: {dev_1.first}, Pay: {dev_1.pay}')

# Only dev_1 gets raise
print(f'dev_2 --> First Name: {dev_2.first}, Pay: {dev_2.pay}')
