# pyright: strict

# '''
# +++++++++++++++++++++++++++++++++
# Let's work with numbers
# We can have Integers and Floats.
# Integer is a hole number
# Float is a decimal

num1: int = 5
print(num1)
print(type(num1))

num2: float = 5.12
print(num2)
print(type(num2))

# +++++++++++++++++++++++++++++++++
# Arithmetic Operators:
# Addition:       3 + 2
# Subtraction:    3 - 2
# Multiplication: 3 * 2
# Division:       3 / 2
# Floor Division: 3 // 2
# Exponent:       3 ** 2
# Modulus:        3 % 2

# Comparisons:
# Equal:            3 == 2
# Not Equal:        3 != 2
# Greater Than:     3 > 2
# Less Than:        3 < 2
# Greater or Equal: 3 >= 2
# Less or Equal:    3 <= 2
# +++++++++++++++++++++++++++++++++

print(2)
print(2.0987)
print(-5.45)
print(3 + 5.45)
print(3 - 5.45)
print(3 / 5.45)
print(3 * 5.45)
print(3 * 4 + 5)
print(3 * (4 + 5))

# use of mod
# takes first number divide it by second and show the reminder
print(10 % 3)


# to check if a number is odd or even mod it by 2
# if the resut is 0, the number is even
# if the resukt is 1, the number is odd
num: int = 43
print(num % 2)


# Convert to string
my_num: int = 5
print(str(my_num))
print(f'{str(my_num)} is my favorite number')

# some number functions
my_num: int = -5
print(abs(my_num))

# a number to the power
print(pow(3, 2))
print(pow(3, 3))

# max & min function
print(max(2, 5, 18, 3, 27, 11))
print(min(2, 5, 18, 3, 27, 11))

# rounding
print(round(3.44))  # round to nearest integer value
print(round(3.54))
print(round(3.54, 1))  # round to the first digit
# +++++++++++++++++++++++++++++++++

# +++++++++++++++++++++++++++++++++
# casting, string to integer
num_1: str = '100'
num_2: str = '200'

print(num_1 + num_2)

num_1: str = '100'
num_2: str = '200'

num_11: int = int(num_1)
num_22: int = int(num_2)

print(num_11 + num_22)
