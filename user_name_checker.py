# Load registered usernames from a file
def load_registered_usernames():
    try:
        with open('registered_usernames.txt', 'r') as file:
            return file.read().splitlines()
    except FileNotFoundError:
        return []


# Save registered usernames to a file
def save_registered_usernames(usernames):
    with open('registered_usernames.txt', 'w') as file:
        for username in usernames:
            file.write(username + '\n')


def check_username(username):
    if username in registered_usernames:
        print("Sorry, the username is already taken. Please choose another username.")
    else:
        registered_usernames.append(username)
        save_registered_usernames(registered_usernames)
        print("Congratulations! You have successfully subscribed.")


def main():
    """docstring"""
    global registered_usernames
    registered_usernames = load_registered_usernames()

    username = input("Enter your desired username: ")
    check_username(username)


if __name__ == "__main__":
    main()