# pyright: strict

# Functions are collection of code to perform specific task
# Help us to oeganize repeated tasks
# Use fucnction to group the code to pefrom specific task
# Think of fuction as a machine that takes some input
# and produce some resuts
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# if you want a function but not ready to work on it use pass


def some_func():
    pass


print(some_func)  # gives the func name at it address in memory
print(some_func())  # returns None
# some_func()
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


def say_hello():
    print("Hello User")


print("Start")
say_hello()
print("Finish")
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


def say_hello1(name: str):
    print(f"Hello {name}")


say_hello1("Mike")
say_hello1("Steve")
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


def say_hello2(name: str, age: float):
    print(f"Hello {name}, you are {age}")


say_hello2("Mike", 35)
say_hello2("Steve", 28.5)
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Treat the return value of a function as a data type
def hello() -> str:
    # return('Hello fuction.') or this approach
    return 'Hello fuction.'


print(hello())
print(len(hello()))
print(hello().upper())
# print(hello()+len(hello()))

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# using default value


def hello5(greet: str, name: str = 'You') -> str:
    return f'{greet}, {name}'


print(hello5('Hi'))
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


def multiply_by_3_v1(num: float) -> float:
    print(num)
    print("still inside function")
    return(3*num)


result = multiply_by_3_v1(4)
print(result)
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


def multiply_by_3_v2(num: float) -> float:
    result: float = 3*num
    return result


result = multiply_by_3_v2(4)
print(result)
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
