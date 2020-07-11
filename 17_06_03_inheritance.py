# pyright: strict
from typing import ClassVar


#  ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#  Inheritance
#  ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
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


# Now, we want our developers have programming language
# So, we need an init method
class Developer(Employee):
    # overwriting the parent
    raise_amt: ClassVar[float] = 1.10

    # We let the parent class handel all the init info except the prog_lang
    def __init__(self, first: str, last: str, pay: int, prog_lang: str) -> None:
        # below handels the first, last, pay
        super().__init__(first=first, last=last, pay=pay)

        # Now we handle the prog_lang
        self.prog_lang: str = prog_lang


dev_1: Developer = Developer('Surush', 'Cyrus', 50000, 'Python')
dev_2: Developer = Developer('Steve', 'Brown', 60000, 'Java')

print(f'dev_1 --> First Name: {dev_1.first}, Prog Lang: {dev_1.prog_lang}')
print(f'dev_2 --> First Name: {dev_2.first}, Prog Lang: {dev_2.prog_lang}')
