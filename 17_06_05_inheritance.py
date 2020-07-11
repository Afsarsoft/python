# pyright: strict
from typing import ClassVar, List, Optional


#  ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
class Employee:

    raise_amt: ClassVar[float] = 1.04  # %4

    def __init__(self, first: str, last: str, pay: int)-> None:
        self.first: str = first
        self.last: str = last
        self.pay: int = pay
        self.email: str = f'{first}.{last}@company.com'

    def fullname(self) -> str:
        return f'{self.first} {self.last}'

    def apply_raise(self) -> None:
        self.pay = int(self.pay * self.raise_amt)
#  ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


#  ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
class Developer(Employee):
    def __init__(self, first: str, last: str, pay: int, prog_lang: str) -> None:
        super().__init__(first=first, last=last, pay=pay)

        self.prog_lang: str = prog_lang
#  ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


#  ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
class ProjectManager(Employee):
    def __init__(self, first: str, last: str, pay: int, project: str) -> None:
        super().__init__(first=first, last=last, pay=pay)

        self.project: str = project
#  ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


# How can I add project mamagers?
#  ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
class Manager(Employee):

    # We let the parent class handel all the init info except the list
    # of Employees this mamager
    def __init__(self, first: str, last: str, pay: int, employees: Optional[List[Developer]] = None) -> None:
        # below handels the first, last, pay
        super().__init__(first=first, last=last, pay=pay)

        # If the argument for employees not provided assign it to empty list
        if employees is None:
            self.employees: List[Developer] = []
        else:
            self.employees: List[Developer] = employees

    def add_emp(self, emp: Developer) -> None:
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp: Developer) -> None:
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self) -> None:
        for emp in self.employees:
            print('Employee -->', emp.fullname())


dev_1: Developer = Developer('Surush', 'Cyrus', 50000, 'Python')
dev_2: Developer = Developer('Steve', 'Brown', 60000, 'Java')

print(f'dev_1 --> First Name: {dev_1.first}, Pay: {dev_1.pay}')
print(f'dev_2 --> First Name: {dev_2.first}, Pay: {dev_2.pay}')


pm_1: ProjectManager = ProjectManager(
    'Kate', 'White', 5000, 'Proj01, Proj02, Proj03')
pm_2: ProjectManager = ProjectManager(
    'Jack', 'Lee', 45000, 'Proj05, Proj06, Proj07')

print(f'pm_1 --> First Name: {pm_1.first}, Pay: {pm_1.pay}')
print(f'pm_2 --> First Name: {pm_2.first}, Pay: {pm_2.pay}')


mgr_1: Manager = Manager('Jane', 'Yang', 80000, [dev_1, dev_2])
mgr_2: Manager = Manager('Bill', 'Jackson', 60000)

print(f'mgr_1 -> Name: {mgr_1.fullname()}, email: {mgr_1.email}')
mgr_1.print_emps()

print(f'mgr_2 -> Name: {mgr_2.fullname()}, email: {mgr_2.email}')
mgr_2.print_emps()

# Adding new Employee
mgr_2.add_emp(dev_2)

print(f'mgr_2 -> Name: {mgr_2.fullname()}, email: {mgr_2.email}')
mgr_2.print_emps()

# Removing an Employee
mgr_1.remove_emp(dev_1)

print(f'mgr_1 -> Name: {mgr_1.fullname()}, email: {mgr_1.email}')
mgr_1.print_emps()
