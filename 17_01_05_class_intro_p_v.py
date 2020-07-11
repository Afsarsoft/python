# pyright: strict


#  ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
class Car:
    def __init__(self, speed: int, color: str) -> None:

        # Private variables
        self.__speed: int = speed
        self.__color: str = color

    def set_speed(self, value: int) -> None:
        self.__speed = value

    def get_speed(self) -> int:
        return self.__speed

    def set_color(self, value: str) -> None:
        self.__color = value

    def get_color(self) -> str:
        return self.__color


toyota: Car
honda: Car
audi: Car

toyota_info: str = ''
honda_info: str = ''
audi_info: str = ''

speed: int = 0
color: str = ''

toyota = Car(200, 'red')
honda = Car(220, 'blue')
audi = Car(250, 'green')

toyota.set_speed(300)
speed = toyota.get_speed()

toyota.set_color('black')
color = toyota.get_color()

toyota_info = f'Car toyota has speed of {speed} and its color is {color}.'
print(toyota_info)
#  ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


#  ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
class Rectangle:
    def __init__(self, height: int, width: int) -> None:
        self.__height: int = height
        self.__width: int = width

    def set_height(self, value: int) -> None:
        self.__height = value

    def get_height(self) -> int:
        return self.__height

    def set_width(self, value: int) -> None:
        self.__width = value

    def get_width(self) -> int:
        return self.__width

    def area(self) -> int:
        return self.__height * self.__width


rect1: Rectangle
rect2: Rectangle

rect1_info: str = ''
rect2_info: str = ''

height: int = 0
width: int = 0
area: int = 0

rect1 = Rectangle(20, 60)
rect2 = Rectangle(50, 40)

rect1.set_height(25)
height = rect1.get_height()

rect1.set_width(65)
width = rect1.get_width()

rect1_info = f'Rectangle rect1 has area of {height * width}.'
print(rect1_info)

area = rect1.area()

rect1_info = f'Rectangle rect1 has area of {area}.'
print(rect1_info)
#  ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
