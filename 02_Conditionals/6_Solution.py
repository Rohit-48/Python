distance = 20

if distance < 3:
    mode = "Walk"
elif  3 < distance < 15:
    mode = "Bike"
else:
    mode = "Car"

print("AI recommends you the transport of:", mode)
