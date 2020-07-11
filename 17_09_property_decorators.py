#  ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#  Property Decorators - Getters, Setters, and Deleters
#  ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@company.com'

    # Regular method
    def fullname(self):
        return f'{self.first} {self.last}'
        # return '{} {}'.format(self.first, self.last)


emp_1 = Employee('Surush', 'Cyrus')
print(
    f'emp_1 --> First Name: {emp_1.first}, email: {emp_1.email}, Full name: {emp_1.fullname()}')

emp_1.first = 'Jim'
print(
    f'emp_1 --> First Name: {emp_1.first}, email: {emp_1.email}, Full name: {emp_1.fullname()}')

# As you see the e-mail did not change by changing the first name
# The fullname does not have this issue. Because becuae everytime we run fullname method it
# grabs the first and last name

# In oder languages like Java they have Getter and Setter for stuf like this
# In Pythod with property decorators we can achive this
'''

'''
# Property decorator allows us to define a method but access it as attribute
# Let's change the new change in our class without breaking any old code


class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def email(self):
        return f'{self.first}.{self.last}@email.com'
        # return '{}.{}@email.com'.format(self.first, self.last)

    # Regular method
    def fullname(self):
        return f'{self.first} {self.last}'
        # return '{} {}'.format(self.first, self.last)


emp_1 = Employee('Surush', 'Cyrus')
print(
    f'emp_1 --> First Name: {emp_1.first}, email: {emp_1.email}, Full name: {emp_1.fullname()}')

emp_1.first = 'Jim'
print(
    f'emp_1 --> First Name: {emp_1.first}, email: {emp_1.email}, Full name: {emp_1.fullname()}')
'''

'''
# We can do simillar approach for full name as well
# Please note that this will break the old code


class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def email(self):
        return f'{self.first}.{self.last}@email.com'
        # return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return f'{self.first} {self.last}'

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last


emp_1 = Employee('Surush', 'Cyrus')
print(
    f'emp_1 --> First Name: {emp_1.first}, email: {emp_1.email}, Full name: {emp_1.fullname}')

emp_1.fullname = 'Jim Smith'
print(
    f'emp_1 --> First Name: {emp_1.first}, email: {emp_1.email}, Full name: {emp_1.fullname}')

# As you see by changing the last name first name, last name, and emil changed
'''

'''
# We can have a deleter as well for fullname to do some cleanups


class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def email(self):
        return f'{self.first}.{self.last}@email.com'
        # return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return f'{self.first} {self.last}'

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print('Delete name!')
        self.first = None
        self.last = None


emp_1 = Employee('Surush', 'Cyrus')
print(
    f'emp_1 --> First Name: {emp_1.first}, email: {emp_1.email}, Full name: {emp_1.fullname}')

emp_1.fullname = 'Jim Smith'
print(
    f'emp_1 --> First Name: {emp_1.first}, email: {emp_1.email}, Full name: {emp_1.fullname}')

del emp_1.fullname
print(
    f'emp_1 --> First Name: {emp_1.first}, email: {emp_1.email}, Full name: {emp_1.fullname}')
'''
