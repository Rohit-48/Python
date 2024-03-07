password = len("Sec")

if (password) < 6:
    strength = "Weak"
elif (password) <= 10:
    strength = "Medium"
else:
    strength = "Strong"

print("Password strength is: ", strength)