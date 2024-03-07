
input_age = int(input("Enter Your Age: ") ) 

input_day = input("Enter Today Day: ")

price = 12 if input_age >= 18 else 8

if input_day == "Wednesday":
     price -= 2

print("Ticket price for you is: $",price)