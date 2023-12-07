# Simple to see how it will identify a
# number as a positive and or negative number
while True:
    try:
        number = float(input("\nEnter a number: "))
        break
    except ValueError:
        print("Invalid input, try again next time.")

if number < 0:
    print("The number is negative")
elif number > 0:
    print("The number is positive")
else:
    print("The number is Zero")
