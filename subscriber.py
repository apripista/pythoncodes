# Open the guest_book.txt file in appended mode
with open('guest_book.txt', 'a') as guest_book:
    while True:
        name = input("Please enter your name (or type 'exit' to quit): ")

        if name.lower() == 'exit':
            break  # Exit the loop if the user types 'exit'

        # Print a greeting to the screen
        print(f"Hello, {name}! Welcome to our site.")

        # Add the entry to the guest book file
        guest_book.write(name + "\n")

print("Thank you for visiting! Your entries have been recorded in guest_book.txt.")