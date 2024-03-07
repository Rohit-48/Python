# 1. Write a program that asks the user for their age and then tells them if they are a child, teenager, adult or senior citizen.
user_age = int(input("Enter your age: "))

if user_age < 13:
    print("You are a child")

elif user_age >= 13 and user_age <= 19:
    print("You are a teenager")

elif user_age >=20 and user_age <= 59:
    print("You are an adult")
elif user_age >= 60:
    print("You are a senior citizen")
