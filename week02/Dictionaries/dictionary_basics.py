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
