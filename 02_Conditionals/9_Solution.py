year = 2025


if (year % 4 == 0) or (year % 400 == 0 and year % 100 != 0 ):
    print(year, "Is a Leap Year")
else:
    print(year,"is NOT Leap Year ")