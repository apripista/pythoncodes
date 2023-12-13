import bcrypt

def load_user_data(filename):
    user_data = {}
    with open(filename, 'r') as file:
        lines = file.read().splitlines()
        for line in lines:
            username, hashed_password = line.split(":")
            user_data[username] = hashed_password
    return user_data

def authenticate_user(username, input_password, user_data):
    if username in user_data:
        stored_hashed_password = user_data[username]
        input_hashed_password = bcrypt.hashpw(input_password.encode('utf-8'), stored_hashed_password.encode('utf-8'))
        return stored_hashed_password == input_hashed_password.decode('utf-8')
    return False

# Load existing usernames and hashed passwords
user_data = load_user_data('usernames.txt')

# User input
user_name = input("Enter your username: ")
input_password = input("Enter your password: ")

if authenticate_user(user_name, input_password, user_data):
    print("Password is correct. Welcome!")
else:
    print("Incorrect password. Access denied.")
