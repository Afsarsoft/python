# pyright: strict

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


def squre(number: float) -> float:
    return number*number


result: float = squre(3)
print(result)
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


def cube(num: float) -> float:
    # return num*num*num
    return pow(num, 3)


result: float = cube(4)
print(result)
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


def convert_to_km(mile: float) -> float:
    return 1.6 * mile


km: float = convert_to_km(5)
print(f"km = {km}")
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# BMI calculator
name1: str = "Surush"
height_ml: float = 1.75
weight_kg1: float = 70

name2: str = "Simin"
height_m2: float = 1.5
weight_kg2: float = 80

name3: str = "Sia"
height_m3: float = 2
weight_kg3: float = 90

# Body mass index (BMI) is a measure of body fat based on height and weight
# that applies to adult men and women.
#
# BMI Categories:
# Underweight = <18.5
# Normal weight = 18.5–24.9
# Overweight = 25–29.9
# Obesity = BMI of 30 or greater


def bmi_calculator(name: str, height_m: float, weight_kg: float) -> str:
    bmi = weight_kg / (height_m ** 2)
    if bmi < 25:
        return f'{name} bmi is {bmi} and is not overweight.'
    else:
        return f'{name} bmi is {bmi} and is overweight'


resutl1 = bmi_calculator(name1, height_ml, weight_kg1)
resutl2 = bmi_calculator(name2, height_m2, weight_kg2)
resutl3 = bmi_calculator(name3, height_m3, weight_kg3)

print(resutl1)
print(resutl2)
print(resutl3)


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Needs to get better, just a start


def is_valid_month(month: int) -> bool:
    # checking between a number
    if not 1 <= month <= 12:
        return False
    else:
        return True


print(is_valid_month(12))
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
