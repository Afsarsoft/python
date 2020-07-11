# pyright: strict


#  ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#  Class methods
#  ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
class Employee:

    def __init__(self, first: str, last: str, pay: int) -> None:
        self.first: str = first
        self.last: str = last
        self.pay: int = pay
        self.email: str = f'{first}.{last}@company.com'

    # Regular method
    def fullname(self) -> str:
        return f'{self.first} {self.last}'

    # We create class mothod by having the following decorator
    # Basically, we are having class as first argument "cls"
    # We cannot use class itself and instead need to use "cls"
    # A class method to pars the string and create a new instance/object
    @classmethod
    def from_string(cls, emp_str: str):
        first: str = ''
        last: str = ''
        pay: str = ''
        pay_result: int = 0

        first, last, pay = emp_str.split('|')
        pay_result = int(pay)
        return cls(first=first, last=last, pay=pay_result)


emp_1: Employee = Employee(first='Surush', last='Cyrus', pay=50000)
print(
    f'emp_1-> Full Name: {emp_1.fullname()}, Pay: {emp_1.pay}, email: {emp_1.email}')


# Some folks using class method as alternative to constructors.
# Basically, they use class methods for creating different instances/objects
# For this purpose, C++ can implement such a feature with overloading,
# but Python lacks this overloading. Instead, we can use classmethod.
# Consider class method from_string
# From a string, we are creating new instance/object Employee
emp_str_2: str = 'Mary|Smith|70000'
emp_2: Employee = Employee.from_string(emp_str_2)
print(
    f'emp23 -> Full Name: {emp_2.fullname()}, Pay: {emp_2.pay}, email: {emp_2.email}')
