"""
MadLibs
Author: Zach Totaro
Period/Core: Core 2
"""
print("Let's play Silly Sentences!\n")
name = input("Enter a name: ")
place = input("Enter a place: ")
food_one = input("Enter a food: ")
food_two = input("Enter another food: ")
adjective_one = input("Enter an adjective: ")
adjective_two = input("Enter another adjective: ")
verb = input("Enter a verb: ")
noun = input("Enter a noun: ")
year = int(input("Enter a year: "))
vehicle = input("Enter a vehicle: ")
drink = input("Enter a drink: ")

print("\n" + name + f" wants to go to {place} to see all of the {adjective_one} {noun}s that {place} is famous for. While {name} is there, they hope to {verb} with all the locals. {name}'s favorite food is {food_one}, esepecially when it's {adjective_two}. They plan on going to a restaurant. {name} hopes that the restaurant also has {food_two} to go with the {food_one}. {name} will leave for {place} tomorrow morning in his {year} {vehicle}. {name} will have to remember to stop and get some {drink} on the way, because it's going to be a long drive.")