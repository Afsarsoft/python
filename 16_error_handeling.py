# pyright: strict

#  ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#   Error handeling
# https://stackoverflow.com/questions/16138232/is-it-a-good-practice-to-use-try-except-else-in-python
#  ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
try:
    age: int = int(input('Age: '))
    print(f'Your age is {age}')

# Base class for all exceptions
except Exception as e:
    print(e)
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Better to provide some info
try:
    age: int = int(input('Age: '))
    print(f'Your age is {age}')

except ValueError as e:
    print(f'Invalid Value! "{e}"')

except Exception as e:
    print(e)
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# income: int = 200_000, be able to read large numbers
try:
    age: int = int(input('Age: '))
    income: int = int(input('Income: '))
    category: int = income / age
    print(f'Age = {age} and Income = {income}. Category = {category}')

except ZeroDivisionError as e:
    print(f'Age cannot be 0! "{e}"')

except ValueError as e:
    print(f'Invalid Value! "{e}"')

except Exception as e:
    print(e)
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Since we do not have the following file, we get error
with open('sometest.txt', 'r') as f:
    pass

try:
    pass
except Exception:
    pass
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Doing the following, we get our custom error and our program is not failing
try:
    with open('sometest.txt', 'r') as f:
        pass

except Exception:
    print('Sorry. This file does not exist!')
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# better way to handel
# Avoid custom and put the obvious handeling error at top
# else-clause runs when there is no exception but before the finally-clause.
# use of finally:
# https://stackoverflow.com/questions/11551996/why-do-we-need-the-finally-clause-in-python
try:
    with open('some test.txt', 'r') as f:
        print(f.read())

except FileNotFoundError as e:
    print(f'Sorry. This file does not exist! Error -> {e}')

except Exception as e:
    print(e)

else:
    print("Executing else...")

finally:
    print("Executing finally...")
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Sometimes you need to raise an exception
try:
    with open('bad_file.txt', 'r') as f:
        if f.name == 'bad_file.txt':
            raise Exception

except FileNotFoundError as e:
    print(e)

except Exception as e:
    print('Error! Opening a bad file!!!')

else:
    print("Executing else...")

finally:
    print("Executing finally...")
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
