while True:
    try:
        year = int(input("Enter any year: "))
        break  # exit a loop if invalid input is entered
    except ValueError:
        print("Invalid year, ")

if year % 100 != 0 and year % 400 == 0 or year % 4 == 0:
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")