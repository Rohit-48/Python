age = 6
species = "cat"

food = "Not defined"
if species == "dog" and age < 2:
    food = "Puppy Food"
elif species == "cat" and age > 5:
    food = "Senior Cat Food"

print(food)