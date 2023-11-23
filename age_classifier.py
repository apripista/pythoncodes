while True:
    try:
        age = int(input("\nEnter your age: "))

        if age < 0:
            print("There is no negative ages")
        if age in range(1):
            print("You are an infant")
        if age in range(2, 3):
            print("Toddler")
        if age in range(4, 6):
            print("Preschooler")
        if age in range(6, 13):
            print("child")
        if age in range(13, 119):
            print("Your are no longer a child, adolescent now")
        if age in range(19, 31):
            print("young adult")
        if age in range(31, 61):
            print("Adult")
        if age in range(61, 100):
            print("senior")

        if age == 100:
            print('You are more blessed!.')

        if age >= 100:
            print(f"I can't believe that you are {age} years old!")

        break

    except ValueError:
        print("Invalid input. Please enter a valid age as a number.")

