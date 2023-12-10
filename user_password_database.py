# Load existing usernames and hashed passwords in a file
with open('usernames.txt', 'r') as username_file:
    lines = username_file.read().splitlines()
    user_data = {}
    for line in lines:
        user_name, hashed_password = line.split(":")
        user_data[user_name] = hashed_password

# Retrieve and display the plain-text password (not recommended)
user_name = input("Enter the username to see the password for: ")

if user_name in user_data:
    hashed_password = user_data[user_name]
    print(f"Plain-text password for {user_name}: {hashed_password}")
else:
    print("Username not found.")
