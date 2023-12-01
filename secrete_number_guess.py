secret_number = 9
try:
    attempt = 3
    print("\nYOU HAVE THREE CHANCES.\n")
    while attempt > 0:
        guess_input = input("Guess a secret number: ")

        if guess_input.lower() == 'quit':
            print("You choose to quit. Goodbye!")
            break

        guess = int(guess_input)  # Convert user input to an integer

        if guess == secret_number:
            print("Congratulations. You win!")
            print("Happy guessing!")
            break  # Exit the loop since the guess was correct
        else:
            print("Sorry, please try again.")

        attempt -= 1
        if attempt == 0:
            print("\nOut of chances and you lose.")

except ValueError:
    print('Invalid input. Please enter a valid number.')
