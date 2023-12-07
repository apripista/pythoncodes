secret_number = 9
try:
    attempt = 3
    print("\nYOU HAVE THREE CHANCES.\n")
    while attempt > 0:
        guess_input = input("Guess a secret number: ")

        if guess_input.lower() == 'quit':  # allow user to quit
            print("You choose to quit. Goodbye!")
            break
        guess = int(guess_input)  # convert the input to integer

        if guess_input == secret_number:
            print("Congratulation. You win")
            print("Happy guessing")
            break  # exit the loop since the guess is correct
        else:
            print("Sorry may you try again.")

        attempt -= 1
        if attempt == 0:
            print("\nOut of chances and you lose.")

except ValueError:
    print('You lose.')