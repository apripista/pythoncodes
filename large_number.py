print("\n A PROGRAM THAT CHECK FOR THE LARGEST NUMBER AMONG THREE NUMBERS ENTERED BY THE USER IN THE KEYBOARD")

# declaring variable for storing data values
first_number = input("enter a first number: ")
second_number = input("enter the second number: ")
third_number = input("enter a third number: ")

# creating condition statements using 'if'
if first_number >= second_number and first_number >= third_number:
    print(f"THE LARGEST NUMBER IS {first_number}")
if second_number >= first_number and second_number >= third_number:
    print(f"THE LARGEST NUMBER IS {second_number}")
if third_number >= first_number and third_number >= second_number:
    print(f"THE LARGEST NUMBER IS {third_number}")
if first_number == third_number and third_number == second_number:
    print("THERE IS NO LARGEST NUMBER ALL OF THEM ARE EQUAL")