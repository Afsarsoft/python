# pyright: strict

'''
#  ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
class Hello:
    def __init__(self, name: str = 'Pete') -> None:  # optional parameter
        print(name)


hello: Hello

hello = Hello()
hello = Hello('Jack')
#  ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
'''


'''
# *args = use when not sure how many arguments might be
#         passed to the function, capture as a tuple
# **kwargs = same as args but captures as dictionary
# The names *args and **kwargs are only by convention and there's no hard requirement to use them.
# Can use both in the same function but *args must occur before **kwargs.
#  ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
class Hello:
    def __init__(self, *args: str) -> None:
        for name in (args):
            print(f'Hello {name}!')


hello: Hello

hello = Hello()
hello = Hello('Jack')
hello = Hello('Jack', 'Mary', 'Bob', 'Sam')
#  ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
'''


'''
class Hello:
    def __init__(self, name: str) -> None:
        self.mame = name
        self.age = 10
        print(f'Hello {name}. You are {self.age} years old!')


hello: Hello
hello = Hello('Jack')
'''
