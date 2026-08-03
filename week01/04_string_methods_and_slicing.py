"""Week 1 practice: string methods, splitting, and slicing."""

text = "Programming is pretty powerful."
print("The letter 'p' appears", text.lower().count("p"), "times.")

mixed = "pYtHoN iS FuN"
print(mixed.capitalize())

message = "   welcome to python   "
print(message.strip())

first_name = "Joey"
favorite_movie = "Avengers"
word = "cybersecurity"
print(first_name[:3])
print(favorite_movie[-3:])
print(word[5:8])

favorite_animal = "I like cats"
print(favorite_animal.replace("cats", "dogs"))

favorite_foods = "sushi, pizza, steak, chicharrones"
food_list = favorite_foods.split(", ")
print(food_list)
print(food_list[2])
