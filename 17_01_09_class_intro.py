# pyright: strict


#  ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Classes allow us to logically group our data and code (attributes and methods).
# When we are dealing with many info related to specific something or subject,
# classes become handy.
# Imagine we have many info related to Employees. Like, Name, Last name,
# Employee ID, Sex, Salary, email, Level, Title, Marital Status, Number of childeren,
# Office Address, Home Address,  Emergency contact….
# For example we want to display Employee information as follow:
'''
name: str = 'Bob'
last_name: str = 'Brown'
employee_id: int = 70398
Sex: str = 'Male'
Salary: int = 70000
email: str = 'BobBrown@hotmail.com'
level: int = 60
title: str = 'Programmer'
martial_status: str = 'Married'
no_of_Childeren: int = 2
office_Address: str = '12/345'
home_address: str = '6732 SE 12th Ave, Redmond, WA, 98053'


def display_employee(name: str,
                     last_name: str,
                     employee_id: int,
                     Sex: str,
                     Salary: int,
                     email: str,
                     level: int,
                     title: str,
                     martial_status: str,
                     no_of_Childeren: int,
                     office_Address: str,
                     home_address: str)-> None:

    message: str = f"""name = {name}, last_name = {last_name}, employee_id = {employee_id},
Sex = {Sex}, Salary = {Salary}, email = {email}, level = {level}, title = {title}
martial_status = {martial_status}, no_of_Childeren = {no_of_Childeren},
office_Address = {office_Address}, home_address = {home_address}"""

    print(message)
'''

# As you see it is difficult to use all these variables into a function.
# Isn’t is better to take all these items to only one variable called Employee?
# As you see it is difficult to use all these variables into a function.
# Isn’t this better to take all these items and put it in only one variable
# called Employee and pass it to our display_employee function?
# By doing this, as we add more info to Employees, we do not need to maintain our function.
# It makes lot easier to add stuff. Classes let us to do that.


class Employee:  # Name of class
    name: str = 'Bob'  # attribute
    last_name: str = 'Brown'  # attribute
    employee_id: int = 70398  # attribute
    Sex: str = 'Male'  # attribute
    Salary: int = 70000  # attribute
    email: str = 'BobBrown@hotmail.com'  # attribute
    level: int = 60  # attribute
    title: str = 'Programmer'  # attribute
    martial_status: str = 'Married'  # attribute
    no_of_Childeren: int = 2  # attribute
    office_Address: str = '12/345'  # attribute
    home_address: str = '6732 SE 12th Ave, Redmond, WA, 98053'  # attribute


# Now I can just pass one variable and access all needed info
def display_employee(some_employee: Employee)-> None:
    message: str = f'{some_employee.name}, {some_employee.last_name}, {some_employee.employee_id}, '
    message += f'{some_employee.Sex}, ...'
    print(message)


# Create an instance of class or object
employee1: Employee = Employee()

# we can access the attributes using dot (.) operator
print(employee1.name)

# We can change the attributes using dot operator
employee1.name = "Jeff"
print(employee1.name)

display_employee(some_employee=employee1)
