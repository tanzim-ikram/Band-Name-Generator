# Day-1: Project-Band Name Generator
# Program will take the name of the City that the User grew up in and his Pet Name as input and will generate a
# Band Name for him/ her.

print("Welcome to the Band Name Generator")
user_name = input("What's your name?\n")
city = input("What's the name of the City that you grew up in?\n")
pet_name = input("What's the name of your Pet?\n")

band_name = city + " " + pet_name
print(user_name + ", here is your Band Name: " + band_name)
