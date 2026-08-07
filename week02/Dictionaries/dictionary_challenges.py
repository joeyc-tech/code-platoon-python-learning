# Create a dictionary called student with the keys name, age, and grade. Assign your own values and print the dictionary.

student = {
    "name" : "Joey",
    "age" : 25,
    "grade" : "Senior"
    }
print(student)

# Print only the value associated with the key name from your student dictionary.
print(student["name"])

# Add a new key called school to the student dictionary and give it a value.

student["school"] = "Code Platoon University"

print(student)

# Change the value of the grade key to a new value.

student["grade"] = "A"

print(student)

# Delete the age key from the school dictionary. 

del student["age"]
print(student)

# Challenge: 
# Modify your dictionary to take input from the user. What parts will you need to put together? 

student = {
#    "name" : input("What is your name?"),
#    "grade" : input("What is your grade?"),
#   "school" : input("What School are you attending?")
    }
#print(student)


# Looping with a dictionary
    # create a dictionary named capitals with the following key-value pairs
    
capitals = {
    "Texas" : "Austin",
    "Florida" : "Tallahassee",
    "California" : "Sacramento",
    "New York" : "Albany"
}
for state, capital in capitals.items():
    print("The capital of", state, "is", capital)

# # Group Challenge

# # Challenge 1: Create a dictionary named animals with some of the following key-value pairs(please add more)

animals = {
    "dog" : "barks",
    "cat" : "meow",
    "cow" : "moo",
    "duck" : "quack",
    "wolf" : "howl",
    "lion" : "roars",
    "pig" : "oink, oink",
    "bird" : "chirp, chirp",
    
}
animal = input("Enter an animal: ").strip().lower()

if animal in animals:
    print(animals[animal])

else:
    print("Animal not found!")


# # Challenge 2: Create an online chatbot for users to access up-to-date menu prices.
# ## create a dictionary named menu with these items and prices ( add more)

menu = {
    "burger" : "$8.99",
    "pizza" : "$12.50",
    "salad" : "$6.75",
    "soda" : "$2.00",
    "hotdog" : "$1.50",
    "water" : "$1.00",
    "soft serve" : "$3.50",
    "chicken fingers" : "$6.25",
    "steak" : "$14.25",
    "grilled chicken" : "$12.25",
    "fries" : "$2.50",
    }
item = input("Enter food item: ").strip().lower()

if item in menu:
    print(menu[item])

else:
    print("Item not available!")