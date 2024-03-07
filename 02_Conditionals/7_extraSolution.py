def customize_coffee(size, extra_shot):
    order = f"{size} coffee"
    if extra_shot:
        order += " with an extra shot of espresso"
    return order

size = input("Enter the size of the coffee (Small, Medium, Large): ")
extra_shot = input("Do you want an extra shot of espresso? (yes/no): ")

if size.lower() in ["small", "medium", "large"]:
    if extra_shot.lower() in ["yes", "no"]:
        coffee_order = customize_coffee(size, extra_shot.lower() == "yes")
        print(f"Your coffee order: {coffee_order}")
    else:
        print("Invalid input for extra shot. Please enter 'yes' or 'no'.")
else:
    print("Invalid input for size. Please enter 'Small', 'Medium', or 'Large'.")
