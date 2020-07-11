# pyright: strict


#  ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#  Classes and Instances
#  ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#  ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Adding a method
class Employee:

    def __init__(self, first: str, last: str, pay: int) -> None:
        self.first: str = first
        self.last: str = last
        self.pay: int = pay
        self.email: str = f'{first}.{last}@company.com'

    # Method for full name
    def fullname(self) -> str:
        return f'{self.first} {self.last}'


emp_1: Employee = Employee(first='Surush', last='Cyrus', pay=50000)
emp_2: Employee = Employee(first='Steve', last='Brown', pay=60000)

print(
    f'emp_1 --> Full Name: {emp_1.fullname()}, Pay: {emp_1.pay}, email: {emp_1.email}')
print(
    f'emp_2 --> Full Name: {emp_2.fullname()}, Pay: {emp_2.pay}, email: {emp_2.email}')
#  ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
