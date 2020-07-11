# pyright: strict


'''
#  ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
class Car:
    def __init__(self) -> None:  # Constructor or initializer of attibutes and methods
        print('in __init__')


# Define objects
toyota: Car
honda: Car
audi: Car

# Create objects
toyota = Car()
honda = Car()
audi = Car()
#  ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
'''


'''
#  ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
class Car:
    def __init__(self, speed: int, color: str) -> None:
        print('in __init__')
        print(speed)
        print(color)


# Define objects
toyota: Car
honda: Car
audi: Car

# Create objects
toyota = Car(200, 'red')
honda = Car(220, 'blue')
audi = Car(250, 'green')
#  ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
'''


'''
#  ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
class Car:
    def __init__(self, speed: int, color: str) -> None:

        # Let’s assigning the attributes of the object to the values we are passing in
        # self keyword basically is the current object.
        # In other languages like C++ or Java we have this keyword
        self.speed: int = speed
        self.color: str = color


toyota: Car
honda: Car
audi: Car

toyota_info: str
honda_info: str
audi_info: str

toyota = Car(200, 'red')
honda = Car(220, 'blue')
audi = Car(250, 'green')

toyota_info = f'Car toyota has speed of {toyota.speed} and its color is {toyota.color}.'
print(toyota_info)

honda_info = f'Car honda has speed of {honda.speed} and its color is {honda.color}.'
print(honda_info)

audi_info = f'Car honda has speed of {audi.speed} and its color is {audi.color}.'
print(audi_info)
#  ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
'''


'''
#  ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
class Rectangle:
    def __init__(self, height: int, width: int) -> None:
        self.height: int = height
        self.width: int = width


rect1: Rectangle
rect2: Rectangle
rect1_info: str
rect2_info: str

rect1 = Rectangle(20, 60)
rect2 = Rectangle(50, 40)

rect1_info = f'Rectangle rect1 has area of {rect1.height * rect1.width}.'
print(rect1_info)

rect2_info = f'Rectangle rect2 has area of {rect2.height * rect2.width}.'
print(rect2_info)
#  ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
'''
