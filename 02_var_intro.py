# pyright: strict

# Why do we need variables?
# considering the following:
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
print("=" * 30)
print("Tom is 50 years old.")
print("=" * 30)
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Here, we are getting error since using integer in string
#age: int = 35
#print("He was " + age + " years old.")

# To fix it, need to do the following:
age: int = 35
print("He was " + str(age) + " years old.")
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# However, no issue using f function
age: int = 35
print(f"Surush was {age} years old.")
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
greeting: str = 'Hello'
name: str = 'Python'

older_message: str = greeting + ', ' + name + '!'
old_message: str = '{}, {}!'.format(greeting, name)

# Python 3.6 and beyond
new_message: str = f'{greeting}, {name}!'

print('Older approach ->', older_message)
print('Old approach ->', old_message)
print('New approach ->', new_message)

# Cool thing about them be able to do as follow:
message = f'{greeting}, {name.upper()}. Welcome!'
print(message)
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# see what is in main Python variables
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
name = "John"    # A string assignment
type(name)          # to learn about type of it
dir(name)           # to learn about the pbject
help(str)           # to learn about the type


counter = 100       # an integer assignment
type(counter)
dir(counter)        # dir(), returns list of the attributes and methods of any object
help(int)

miles = 1000.0       # A floating point
type(miles)
dir(miles)
print("=" * 30)
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Switch the values of 2 variables
v1 = "first string"
v2 = "second string"

temp = v1
v1 = v2
v2 = temp

print(v1)
print(v2)
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
