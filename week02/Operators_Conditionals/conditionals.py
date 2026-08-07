# Conditional Examples
# response.strip() will allow spaces in the user input

response = input("What do you want for dinner?")
response = response.strip()

if response == "sushi":
    print("Let's go to Tai Fai!")
elif response == "pizza":
    print("Let's go to to Jets")
elif response == "mexican":
    print("lets go to Mi Casita")
else:
    print("Alright, lets do leftovers")



# Multiple IF statements

x = 3
if (x > 2):
    x=x * 2;
if (x > 4):
    x = 0;
    print(x)

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