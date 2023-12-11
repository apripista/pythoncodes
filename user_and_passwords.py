import bcrypt

# Load existing usernames
with open('usernames.txt', 'r') as username_file:
    registered_usernames = username_file.read().splitlines()

# Open usernames.txt and add a new username along with a hashed password
with open('usernames.txt', 'a') as username_file:

    while True:
        print("Press 'quit' or 'q' or 'e' to exit")
        user_name = input("Write your username: ")

        if user_name.lower() in ['q', 'e', 'quit']:
            print("You opted to exit")
            print("Goodbye!")
            break

        if user_name in registered_usernames:
            print(f"Username {user_name} is already taken. Please choose another username.\n")
            continue

        password = input("Enter your password: ")
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

        print(f"Hello {user_name}, Welcome to the channel")
        username_file.write(f"{user_name}:{hashed_password.decode('utf-8')}\n")

        print(f"{user_name}, Congratulations, you have been added\n")
