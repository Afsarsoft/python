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

    @classmethod
    def set_raise_amt(cls, amt: float) -> None:
        cls.raise_amt = amt


emp_1: Employee = Employee(first='Surush', last='Cyrus', pay=50000)
emp_2: Employee = Employee(first='Steve', last='Brown', pay=60000)

# Let's increase raise_amt using our new class method set_raise_amt
Employee.set_raise_amt(1.05)

# We get the same result from the object/instance!!. What is the point?
# emp_1.set_raise_amt(1.05)

# Increased for all
print(f'Class -> raise_amt: {Employee.raise_amt}')
print(f'emp_1 -> raise_amt: {emp_1.raise_amt}')
print(f'emp_2 -> raise_amt: {emp_2.raise_amt}')
