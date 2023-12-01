# open guests.txt file in ready only mode
with open('guests.txt', 'r') as guest:
    registered_users = guest.read().splitlines()

# open a guests.txt file in append mode and add a new name on it.
with open('guests.txt', 'a') as username_file:
    while True:
        print("Press 'quit' 'q' or 'e' to exit when you are ready.")  # user can choose to quit
        user_name = input("what is your username: ")  # username prompt

        if user_name in ['quit', 'q', 'e']:  # quiting condition
            print("You choose to exit.")
            print("Goodbye!")
            break  # exit the loop (exit checker)

        if user_name in registered_users:
            print(f"username '{user_name}', already taken. Please choose another username\n")
            continue  # users are allowed to choose another username

        print(f"Hello {user_name} Thank you for subscribing in my channel.\n")
        username_file.write(user_name + '\n')

        print(f"{user_name}, please invite your friends too.")