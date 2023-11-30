secret_number = 5
try:
    attempt = 3
    while attempt > 0:
        guess_input = int(input("Guess a secret number: "))
        if guess_input == secret_number:
            print("Congratulation!, You win.")
            print("Happy guessing.")
            break
        else:
            print("Try again")
            attempt -= 1
        if attempt == 0:
            print("Out of chances, You are a loser")

except ValueError:
    print("Invalid format")
