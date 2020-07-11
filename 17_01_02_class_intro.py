# pyright: strict


#  ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#  Why classes?
#  ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Classes allow us to logically group our data and code (attributes and methods).
class Car:
    pass  # use pass for empty class


# Define objects
toyota: Car
honda: Car
audi: Car

# Create objects
# We create objects based on Classes
# Note: Object or instance of class car
toyota = Car()
honda = Car()
audi = Car()

print(toyota)
print(honda)
print(audi)

print(type(toyota))


#  ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
class Rectangle:
    pass


# Define objects
rectangle1: Rectangle
rectangle2: Rectangle
rectangle3: Rectangle

# Create objects
rectangle1 = Rectangle()
rectangle2 = Rectangle()
rectangle3 = Rectangle()
#  ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
