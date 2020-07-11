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

    def get_increase_speed(self) -> int:
        return self.__add_speed()

    # private method
    def __add_speed(self)-> int:
        return self.__speed + 1

    def set_color(self, value: str) -> None:
        self.__color = value

    def get_color(self) -> str:
        return self.__color


toyota: Car
toyota_info: str = ''
speed: int = 0
color: str = ''

toyota = Car(200, 'red')

toyota.set_speed(300)
speed = toyota.get_speed()

toyota.set_color('black')
color = toyota.get_color()

toyota_info = f'Car toyota has speed of {speed} and its color is {color}.'
print(toyota_info)

speed = toyota.get_increase_speed()
toyota_info = f'Car toyota has speed of {speed} and its color is {color}.'
print(toyota_info)
#  ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
