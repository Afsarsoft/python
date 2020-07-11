#  ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#  Special methods
#  ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
'''
class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = self.first + '.' + self.last + '@company.com'

    # Regular method
    def fullname(self):
        return f'{self.first} {self.last}'
        #return '{} {}'.format(self.first, self.last)

emp_1 = Employee('Surush', 'Cyrus', 50000)
emp_2 = Employee('Steve', 'Brown', 60000)

# Based on above class, the following givs us no much info about our class 
print(emp_1)
'''

'''
# we can change this behaviour to print out some useful information 
# Special methods can help with this need
# Special methods are surounded by double undersores "__" like __init__  
# Two special methods that we should use in our classes are __repr__ and __str__
# Beside below examples, the good reference is https://docs.python.org/3/reference/datamodel.html#special-method-names

class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = self.first + '.' + self.last + '@company.com'

    # Regular method
    def fullname(self):
        return f'{self.first} {self.last}'
        #return '{} {}'.format(self.first, self.last)

    
    # Unambiguous representation of the object
    # Used for developers for debuging and logging 
    # At the minimum, we need to have the repr 
    # If we do not have str, if called str falls back to repr
    # We use here some code to recreate the object
    def __repr__(self):
        return f"Employee('{self.first}', '{self.last}', {self.pay})"

    # Readable representation of the object 
    # used to display to the users
    def __str__(self):
        return f'{self.fullname} - {self.email}'

    # Just for demo other __ capability 
    # Let's add salary of two employees
    def __add__(self, other):
        return self.pay + other.pay 

    # Just for demo other __ capability 
    # maybe someone wants to know how much characters name of employee captures
    def __len__(self):
        return len(self.fullname())

emp_1 = Employee('Surush', 'Cyrus', 50000)
emp_2 = Employee('Steve', 'Brown', 60000)

print('Adding salary of emp_1 and emp_2= ', emp_1 + emp_2)
print('Total character number of emp_1 = ', len(emp_1))

# Before we had "<__main__.Employee object at 0x04626E70>", now, 
# if we have only rpr,  
# we get some meaningfull info "Employee('Surush', 'Cyrus', 50000)"
# this exactly what we used to create the emp_1 object above
# if we have also str,
# We get the friendly version info    
#print(emp_1)

# We still have full access to below as well
#print(repr(emp_1))
#print(str(emp_1))

# Also, we can print out then directly 
#print(emp_1.__repr__())
#print(emp_1.__str__())
'''





