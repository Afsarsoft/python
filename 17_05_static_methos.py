# pyright: strict
from datetime import date


#  ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#  Static methods
#  ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#  ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Static methods do not pass anything instances or class.
# They behave like regular functions
# The reason we adding them to class becuase they have some logical connections with class
class Employee:

    def __init__(self, first: str, last: str, pay: int) -> None:
        self.first: str = first
        self.last: str = last
        self.pay: int = pay
        self.email: str = f'{first}.{last}@company.com'

    # Regular method
    def fullname(self) -> str:
        return f'{self.first} {self.last}'

    # We create static method using following decorator
    # Let's check for work day
    @staticmethod
    def is_workday(day: date) -> bool:
        if day.weekday() == 5 or day.weekday() == 6:  # checking for Saturday and Sunday
            return False
        return True


emp_1: Employee = Employee(first='Surush', last='Cyrus', pay=50000)
emp_2: Employee = Employee(first='Steve', last='Brown', pay=60000)

# Testing our new static method
my_date1: date = date(2018, 12, 23)  # Sunday
print(f'Is {my_date1} a work day? {Employee.is_workday(my_date1)}')

my_date2: date = date(2018, 12, 24)  # Monday
print(f'Is {my_date2} a work day? {Employee.is_workday(my_date2)}')
