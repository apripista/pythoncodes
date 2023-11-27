try:
    print("\nTHE EVEN NUMBER DETECTOR PROGRAM USING PYTHON")
    while True:
        number = int(input("ENTER A NUMBER: "))
        if number % 2 == 0:
            print(f"{number} the number is even")
            continue

        else:
            print("THE NUMBER IS NOT AN EVEN NUMBER, TRY AGAIN TO OTHER NUMBER")
except ValueError:
    print("Invalid value")