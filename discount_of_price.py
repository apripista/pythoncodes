# discount checker in a shop

print("\nTHE PYTHON PROGRAM THAT HELP CUSTOMERS TO CALCULATE THE AMOUNT PAID AFTER THE DISCOUNT")

# declaring the variables and asking users to input their needs
actual_amount = float(input("\n ENTER THE AMOUNT BEFORE DISCOUNT:  "))
discount_rate = float(input("ENTER THE DISCOUNT RATE FOR YOUR PRICE (in percentages):  "))

# calculating the amount payable after the discount has offered
discount_amount = actual_amount * (discount_rate / 100)
total_amount = actual_amount - discount_amount

# displaying the discount amount and the amount after discount is offered if possible
print(f"DISCOUNT AMOUNT IS {discount_amount}")
print(f"THE AMOUNT AFTER DISCOUNT IS {total_amount}")