import bcrypt

# Load existing usernames and hashed passwords
user_data = {}  # Dictionary to hold username-hashed password pairs
with open('usernames.txt', 'r') as username_file:
    lines = username_file.read().splitlines()
    for line in lines:
        user_name, hashed_password = line.split(":")
        user_data[user_name] = hashed_password

# Open usernames.txt and add a new username along with a hashed password
with open('usernames.txt', 'a') as username_file:

    while True:
            print("Press 'quit' or 'q' or 'e' to exit")
            user_name = input("Write your username: ")

            if user_name.lower() in ['q', 'e', 'quit']:
                print("You opted to exit")
                print("Goodbye!")
                break

            if user_name in user_data:
                print(f"Username {user_name.lower()} is already taken. Please choose another username.\n")
                continue

            password = input("Enter your password: ")
            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

            print(f"Hello {user_name.lower()}, Welcome to the channel")
            username_file.write(f"{user_name.lower()}:{hashed_password.decode('utf-8')}\n")
            user_data[user_name] = hashed_password.decode('utf-8')

            print(f"{user_name.lower()}, Congratulations, you have been added\n")