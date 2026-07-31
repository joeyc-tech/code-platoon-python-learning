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

str1 = "hello"
str2 = ","
str3 = "world"
print(str1[-1:])



# 1 Create a string with your first name. Print the first three letters using slicing

first_name = "Joey"
print(first_name[0:3])

# 2 Create a string with your favorite movie. Print the last 3 characters.

fav_movie = "Avengers"
count = len(fav_movie)
print(count)
print(fav_movie[-3:])

# 3 Create the string "CyberSecurity" and print "sec" using slicing

job = "cybersecurity"
print(job[5:8])

# 1 Create the string "I like cats" and replace "cats" with "dogs"

fav_animal = "I like cats"

updated_text = fav_animal.replace("cats", "dogs", 1)

print(updated_text)

# 2 create a sentence with a typo and use .replace() to fix it.

fav_sentence = "I like learning pithon."
update_text = fav_sentence.replace("pithon", "python", 1)

print(fav_sentence.replace("pithon" , "python"))

# 3 Create a string containing your favorite color. Replace it with a new color.

fav_color = "blue"
print(fav_color.replace("blue", "green", 1))

# 4 Write a word of your choice 4 times. Replace it twice with another word.

text = "hello hello hello hello"
update_text = text.replace("hello", "see you later", 2)
print(update_text)

# 1 create. string containing your favorite foods separated by commas. use .split () to create a list

fav_foods = "sushi, pizza, steak, chicharrones"
food_list = fav_foods.split(", ")

print(food_list)
print(food_list[2])


# Split the string "Python is fun" into three separate elements.

sentence = "python is fun"
words = sentence.split(" ")
print(words)


# Harder: Create a sentence and print the first word after using .split(). Try this resource: https://www.w3schools.com/python/python_lists_access.asp 

sentence = "I love learning Python"
words = sentence.split()
print(words[0])



# ✨  Integers and Floats 
# Calculator
def add(num1, num2): 
    return num1 + num2

print(add(1, 13))


def sub(num1, num2): 
    return num1 - num2  

num3 = int(input("enter a number: "))
num4 = int(input("enter another number: "))
print(sub(num3, num4))


# ✨ Math

import math

students = "mark, itzel, Latoya, Joey, Jason, Alice"
list_students = students.split(",")

print(list_students)

# Generte a random number

import random
number = random.randint(0,5)

# output a random student

print(list_students[number])
#  🎯 Try It 
# Ask the user to enter a decimal number. Display the number rounded up using math.ceil() and rounded down using math.floor().

number = 3.14
print(math.ceil(number))
print(math.floor(number))


# Challenge:
# Ask the user to enter a number.
# Calculate and display:
# The square root using math.sqrt()
# The number raised to the power of 2 using math.pow()
# The number raised to the power of 3 using math.pow()
# The absolute value using abs()
# The rounded number using round()
# The ceiling value using math.ceil()
# The floor value using math.floor()
# Round decimal answers to 2 decimal places.


import math
number = float(input("Enter a number: "))
square_root = round(math.sqrt(number),2)
print("square_root", square_root)

power_two = round(math.pow(number, 2), 2)
print("squared:", power_two)

power_three = round(math.pow(number, 3), 2)
print("Cubed:", power_three)

absolute = abs(number)
print("Absolute value:", absolute)

rounded = round(number)
print("Rounded:", rounded)

ceiling = math.ceil(number)
print("Ceiling:", ceiling)

floor = math.floor(number)
print("Floor:", floor)


# ✨ Boolean

print(3 >4)

print(4 !=5)

print(16 == "16")

# even vs odd

num_odd = 66

print(num_odd % 2 ==0)



#  🎯 Try It 

# Ask the user to enter their age. Use a Boolean expression to determine if they are old enough to vote (18 or older).

age = int(input("Enter your age:"))
print("Can vote?", age>=18)



# Ask the user to enter a number. Use Boolean operators to check if the number is positive.

number = float(input("Enter a number: "))

is_positive = number > 0

print("Is the number positive?", is_positive)


