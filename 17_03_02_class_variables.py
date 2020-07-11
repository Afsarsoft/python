# pyright: strict
from typing import ClassVar


#  ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#  Class Variables
#  ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#  ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Let's take a look an example that we do not want have a class variable as self
# Here we want to keep track of number of the employees
class Employee:

    # The number of employees
    num_of_emps: ClassVar[int] = 0
    raise_amt: ClassVar[float] = 1.04  # %4

    def __init__(self, first: str, last: str, pay: int) -> None:
        self.first: str = first
        self.last: str = last
        self.pay: int = pay
        self.email: str = f'{first}.{last}@company.com'

        # The number of employees should be simillar to all the instances
        # will do it in init method since init method runs each time we create new instance(employee)
        # note that we do not have as "self.num_of_emps += 1" since we do not want total number of
        # the employees be different in any instance
        Employee.num_of_emps += 1

    def fullname(self) -> str:
        return f'{self.first} {self.last}'

    def apply_raise(self) -> None:
        self.pay = int(self.pay * self.raise_amt)


# It returns 0 since we do not have any employees yet
print(f'Total number of employees -> {Employee.num_of_emps}')

emp_1: Employee = Employee(first='Surush', last='Cyrus', pay=50000)
emp_2: Employee = Employee(first='Steve', last='Brown', pay=60000)

# It returns 2 since we already created two employees above
print(f'Total number of employees -> {Employee.num_of_emps}')

# It can be accesable from the objects
print(emp_1.num_of_emps)
print(emp_2.num_of_emps)

# The following will effect the object but not the class
emp_1.num_of_emps = 1
print(emp_1.num_of_emps)
print(Employee.num_of_emps)
