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


