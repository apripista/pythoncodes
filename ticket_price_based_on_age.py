print("A PROGRAM TO CALCULATE THE PAYABLE AMOUNT OF A PASSENGER BASED ON AGE")
while True:
    try:
        age = float(input("\nEnter your age: "))
        break
    except ValueError:
        print("Invalid age, try again")

if age <= 5:
    cost = 0.00
    print(f"Your travel cost is:  $ {cost}")
if 5 < age <= 10:
    cost = 15.0
    print(f"Your travel cost is:  $ {cost}")
if 10 < age <= 20:
    cost = 25
    print(f"Travel cost is:  $ {cost}")
if 21 < age <= 30:
    cost = 35
    print(f"Travel cost is:  $ {cost}")
if 31 < age <= 50:
    cost = 45
    print(f"Travel ost is:  $ {cost}")
if age > 50:
    print("You may travel free")
