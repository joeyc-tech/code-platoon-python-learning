"""Week 1 practice: defining and calling functions."""


def say(message, times=1):
    print(message * times)


def greet():
    print("Hello there!")


def welcome(name):
    print(f"Welcome, {name}!")


def square(number):
    return number * number


def add_numbers(number1, number2):
    return number1 + number2


def is_even(number):
    return number % 2 == 0


say("Hello")
say("world ", 5)
greet()
welcome("Joey")
print(square(5))
print(add_numbers(3, 4))
print(is_even(6))
print(is_even(7))
