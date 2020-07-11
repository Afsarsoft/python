# pyright: strict
from typing import ClassVar


#  ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#  Class Variables
#  ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Class variables are shared amoung all instances of a class
# for example, annual raise for all employees
# Instance variables are unique for each instance
# for example, Employee name and email
#  ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
class Employee:

    # Class variable
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


emp_1: Employee = Employee(first='Surush', last='Cyrus', pay=50000)
emp_2: Employee = Employee(first='Steve', last='Brown', pay=60000)
#  ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


#  ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Before and after the raise
print(f'Employee 1, before raise -> Pay: {emp_1.pay}')
emp_1.apply_raise()
print(f'Employee 1, after raise -> Pay: {emp_1.pay}')
#  ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


#  ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# all the same, shared amoung all instances
print(f'Class -> raise_amt: {Employee.raise_amt}')
print(f'emp_1 -> raise_amt: {emp_1.raise_amt}')
print(f'emp_2 -> raise_amt: {emp_2.raise_amt}')
#  ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


#  ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# There is no raise_amt
print(emp_1.__dict__)

# There is raise_amt in the class
print(Employee.__dict__)
#  ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#  ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Here is an important concept
# Let's increase raise_amt in class
Employee.raise_amt = 1.05

# As you see it raised it for all (class and and all the intstances)
print(f'Class -> raise_amt: {Employee.raise_amt}')
print(f'emp_1 -> raise_amt: {emp_1.raise_amt}')
print(f'emp_2 -> raise_amt: {emp_2.raise_amt}')
#  ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


#  ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Let's increase raise_amt again only for an instance
emp_1.raise_amt = 1.07

# As you see it raised it only for emp_1
print(f'Class -> raise_amt: {Employee.raise_amt}')
print(f'emp_1 -> raise_amt: {emp_1.raise_amt}')
print(f'emp_2 -> raise_amt: {emp_2.raise_amt}')
#  ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


#  ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# when we did the "emp_1.raise_amt = 1.07", it created raise_amount for emp_1
# the new "raise_amt = 1.07" is private for emp_1
print(emp_1.__dict__)

# But not for emp_2, emp_2 is using and sharing from the class
print(emp_2.__dict__)

# as you see here, it make sence to use the class variable
# raise_amt as self.raise_amt in the class
#  ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
