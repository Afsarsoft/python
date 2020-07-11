# pyright: strict

# ++++++++++++++++++++++++++++++
# Comparisons:
# Equal:            ==
# Not Equal:        !=
# Greater Than:     >
# Less Than:        <
# Greater or Equal: >=
# Less or Equal:    <=
# Object Identity:  is

# False Values:
# False
# None
# Zero of any numeric type
# Any empty sequence. For example, '', (), [].
# Any empty mapping. For example, {}.
# ++++++++++++++++++++++++++++++

# +++++++++++++++++++++++++++++++++
num1: int = 1
num2: int = 2
if num1 < num2:
    print("num1 is smaller than num2")
    print("num1 is still smaller than num2")
print("not sure if num1 is smaller than num2")
# +++++++++++++++++++++++++++++++++

# +++++++++++++++++++++++++++++++++
num1: int = 5
num2: int = 2
if num1 < num2:
    print("num1 is smaller than num2")
else:
    print("num1 is not smaller than num2")
print("outside the if")
# +++++++++++++++++++++++++++++++++

# +++++++++++++++++++++++++++++++++
if True:
    print('Condition was True')

language: str = 'Python'
if language == 'Python':
    print('Language is Python')
else:
    print('No match')
# +++++++++++++++++++++++++++++++++

# +++++++++++++++++++++++++++++++++
temperature: int = 30

if temperature > 30:
    print("It's a hot day")
else:
    print("It's not a hot day")
# +++++++++++++++++++++++++++++++++

# +++++++++++++++++++++++++++++++++
language: str = 'C#'
if language == 'Python':
    print('Language is Python')
elif language == 'Java':
    print('Language is Java')
elif language == 'C#':
    print('Language is C#')
else:
    print('No match')
# +++++++++++++++++++++++++++++++++

# +++++++++++++++++++++++++++++++++
price: int = 1000000
has_good_credit = False  # True & False

if has_good_credit:
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price

print(f'Down Payment : ${down_payment}')
# +++++++++++++++++++++++++++++++++

# +++++++++++++++++++++++++++++++++
has_high_income: bool = True  # True & False
has_good_credit: bool = False  # True & False

if has_good_credit and has_high_income:
    print('Eligible for loan')
else:
    print('Not eligible for loan!')
# +++++++++++++++++++++++++++++++++

# +++++++++++++++++++++++++++++++++
has_good_credit: bool = True      # True & False
has_criminal_record: bool = False  # True & False

if has_good_credit and not has_criminal_record:
    print('Eligible for loan')
else:
    print('Not eligible for loan!')
# +++++++++++++++++++++++++++++++++

# +++++++++++++++++++++++++++++++++
user: str = 'Admin'
logged_in: bool = True  # True & False

if user == 'Admin' and logged_in:
    print('Admin Page')
else:
    print('Bad Creds!')
# +++++++++++++++++++++++++++++++++

# +++++++++++++++++++++++++++++++++
user: str = 'Admin'
logged_in: bool = True  # True & False

if logged_in:
    print('Welcome')
else:
    print('Please Log In')
# +++++++++++++++++++++++++++++++++

# +++++++++++++++++++++++++++++++++
name: str = "James"

if len(name) < 3:
    print('Name must be at least 3 character!')
elif len(name) > 50:
    print('Name must be a maximum of 50 character!')
else:
    print('Name looks good!')
# +++++++++++++++++++++++++++++++++

# +++++++++++++++++++++++++++++++++
name: str = "Surush"
hight_m: float = 1.7
weight_kg: float = 70
bmi = weight_kg / (hight_m ** 2)
#bmi = weight_kg / (hight_m * hight_m)
print("bmi: ")
print(bmi)

print(name)
if bmi < 25:
    print("is not overweight")
else:
    print("is overweight")
# +++++++++++++++++++++++++++++++++
