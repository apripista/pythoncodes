import bcrypt

# Load existing usernames and hashed passwords
user_data = {}
with open('usernames.txt', 'r') as username_file:
    lines = username_file.read().splitlines()
    for line in lines:
        username, hashed_password = line.split(":")
        user_data[username] = hashed_password

# User input
user_name = input("Enter your username: ")
input_password = input("Enter your password: ")

if user_name in user_data:
    stored_hashed_password = user_data[user_name]

    # Hash the input password with the same salt used before
    input_hashed_password = bcrypt.hashpw(input_password.encode('utf-8'), stored_hashed_password.encode('utf-8'))

    # Compare the hashed input password with the stored hash
    if stored_hashed_password == input_hashed_password.decode('utf-8'):
        print("Password is correct. Welcome!")
    else:
        print("Incorrect password. Access denied.")
else:
    print("Username not found.")
