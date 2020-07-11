# pyright: strict


#  ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#  Classes and Instances
#  ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Classes allow us to logically group our data and code (attributes and methods).
# We create objects based on Classes
# An attribute is a variable that is looked up on another object using dot syntax obj.attribute
# Methods are functions which associated with a class
# Making an object from a class is called instantiation
# We work with instances of a class
# Using classes make our progam easier. Also, they make extending our program easier
# Employee is a good example for a class since each employee have
# name, e-mail, pay, and actions (attributes and methods) which need to perform.
# So, it is good to have a Class can be used as a blue print for all employees
#  ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
class Employee:

    # Need a special init method (initializer), in other languages call it constructor
    # We receive the instance as first argument automatically. By convention called it "self"
    # we can call it anyhing we want but better keep the Python convention
    def __init__(self, first: str, last: str, pay: int) -> None:

        # "self.first" is an instance variable, unique for each instance
        # "first" is the argument passed to our class
        # Basically, we are assigning the attributes of the object to values we are passing in
        self.first: str = first
        self.last: str = last
        self.pay: int = pay
        self.email: str = f'{first}.{last}@company.com'


# In here emp_1 gets pass to Employee class as "self"
# and parameters gets assign to arguments
emp_1: Employee = Employee(first='Surush', last='Cyrus', pay=50000)
emp_2: Employee = Employee(first='Steve', last='Brown', pay=60000)

print(
    f'emp_1 --> First Name: {emp_1.first}, Last Name: {emp_1.last}, Pay: {emp_1.pay}, email: {emp_1.email}')
print(
    f'emp_2 --> First Name: {emp_2.first}, Last Name: {emp_2.last}, Pay: {emp_2.pay}, email: {emp_2.email}')
#  ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
