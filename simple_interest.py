print("\n A PYTHON PROJECT TO CALCULATE THE SIMPLE INTEREST (I = PRT/100)")
print("PROVIDED THAT THE USER HAS ENTERED THE REQUIRED INFORMATION LIKE")
print("TIME OF INTEREST, INTEREST RATE and THE PRINCIPLE AMOUNT\n")

# declaring a variable
principal = float(input('ENTER THE PRINCIPAL AMOUNT YOU WANT TO DEPOSIT:  '))
rate = float(input('ENTER THE RATE OFFERED BY THE COMPANY:  '))
time = float(input('ENTER THE TIME OF YOUR INTEREST(years):  '))

# calculating the simple interest
simple_interest = float(principal * rate * time) / 100

print(f"\n SMPLE INTEREST IS {simple_interest}")
