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




 # 1 define a function called greet() that prints "Hello there!" and call the function
def greet():
    print("Hello there!")

greet()


# 2 Create a function called welcome(name) that prints Welcome, <name>!
def welcome(name):
    print(f"Welcome, {name}!")

welcome("Joey")


# 3 create a function called square() that takes one number as a parameter and returns its square.
def square(number):
    return number * number

print(square(5))


# 4 Write a function called add_numbers() that accepts two numbers and returns their sum.
def add_numbers(number1, number2):
    return number1 + number2

print(add_numbers(3, 4))


# 5 — Spicy 
def is_even(number):
    return number % 2 == 0

print(is_even(6))
print(is_even(7))




# 1. Create two string variables and concatenate them into one sentence.
first = "Joey"
second = " is learning python"
sentence = first + "" + second
print(sentence)


# 2. Create variables for a favorite food and drink.
# Use an f-string to create a complete sentence.

food = "pizza"
drink = "coke zero"
print(f"My favorite food is {food} and my favorite drink is {drink}.")


# 3. Ask the user for their name using input() and greet them with an f-string.

name = input("What is your name? ")
print(f"Hello, {name}! Nice to meet you.")



# 4. Create a sentence and use .count() to count how many times a letter appears.

text = "Programming is pretty powerful."
print("The letter 'p' appears", text.lower().count("p"), "times.")


# 5. Create a string with mixed capitalization and use .capitalize().

mixed = "pYtHoN iS FuN"
print(mixed.capitalize())


# 6. Try out another string method of your choice.

message = "   welcome to python   "
print(message.strip())

# 1. Create a string with your first name.
# Print the first three letters using slicing.

first_name = "Joey"
print(first_name[:3])

# 2. Create a string with your favorite movie.
# Print the last three characters.

favorite_movie = "Avengers"
print(favorite_movie[-3:])

# 3. Create the string "cybersecurity"
# Print "sec" using slicing.

word = "cybersecurity"
print(word[5:8])