"""Week 1 practice: arithmetic, math functions, and booleans."""

import math


def add(number1, number2):
    return number1 + number2


def subtract(number1, number2):
    return number1 - number2


print(add(1, 13))
print(subtract(10, 4))

number = 3.14
print("Square root:", round(math.sqrt(number), 2))
print("Squared:", round(math.pow(number, 2), 2))
print("Cubed:", round(math.pow(number, 3), 2))
print("Ceiling:", math.ceil(number))
print("Floor:", math.floor(number))

age = 41
print("Can vote?", age >= 18)
print("Is the number positive?", number > 0)
print("Is 66 even?", 66 % 2 == 0)
