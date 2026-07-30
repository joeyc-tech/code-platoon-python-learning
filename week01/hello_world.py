dog_age = 7
print(dog_age)
print("Hello, Joey")

print('Hello world!')

dog_age = 7
print(dog_age)

print(type(100))
print(type("100"))

favorite_number = 7
print(favorite_number)
print(type(favorite_number))

favorite_food = "Pizza"
print(favorite_food)
print(type(favorite_food))

is_student = True
print(type(is_student))

print(type(5.0))


def say(message, times=1):
    print(message*times)

say("Hello")
say("world ", 5)

# 1
def greet():
    print("Hello there!")

greet()


# 2
def welcome(name):
    print(f"Welcome, {name}!")

welcome("Joey")


# 3
def square(number):
    return number * number

print(square(5))


# 4
def add_numbers(number1, number2):
    return number1 + number2

print(add_numbers(3, 4))


# 5 — Spicy
def is_even(number):
    return number % 2 == 0

print(is_even(6))
print(is_even(7))
