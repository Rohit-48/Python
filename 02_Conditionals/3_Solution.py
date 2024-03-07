score = int(input("Enter Your Score: "))

if score >= 101:
    print("Please Valid Score")
    exit()

if score >= 90:
    print("Your Grade is A")
elif  score >= 80:
    print("Your Grade is B")
elif  score  >= 70:
    print("Your Grade is C")
elif  score  >= 60:
    print("Your Grade is D")
else:
    print("Your Grade is F")