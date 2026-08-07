user = {
    "name": "Jordan",
    "age": 28
}

# Getting a value

print(user["name"])
print(user.get("name"))

# Add a value
user["major"] = "biology"
print(user["major"])

user["email"] = "ilovepython@gmail.com"
print(user)

# Delete a value

del user ["email"]
print(user)

# updating a value

user ["age"] = 29
print(user)

## MySpace ##

my_space = {
    "username": "ajs1fan",
    "email": "ilovepython@gmail.com",
    "age" : 25,
    "location" : "California",
    "has music" : True,
}

# Check my location

print(my_space["location"])

# add to page

my_space["has_photo"] = True

print(my_space)



# # what will the output of the following Python code?

d1 = {"a" : 1, "b": 2}
d2 = {"b": 3, "c" : 4}
d1.update(d2)
print(d1["b"])
#3
# Reviewing of Conditionals & Dictionaries

employee = {
    "name" : "Ruthie Cohen",
    "title" : "cashier",
    "salary" : "50000"
}
print(employee)

# for keys in dictionary

dict1 = {
    1: "Alpha",
    2: "Bravo",
    3: "Charlie"
}
for num in dict1:
    print(dict1[num])
