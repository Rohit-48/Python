score = int(input("Enter Your Score: "))

if score >= 90:
    print("Your Grade is A")
elif 80 <= score <= 89:
    print("Your Grade is B")
elif 70 <= score <= 79:
    print("Your Grade is C")
elif 60 <= score <= 69:
    print("Your Grade is D")
else:
    print("Your Grade is F")
