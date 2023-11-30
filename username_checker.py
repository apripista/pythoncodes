# open usernames.txt file in ready only mode.
with open('usernames.txt', 'r') as username_file:
    registered_usernames = username_file.read().splitlines()


# open usernames.txt and add a new username to it.
with open('usernames.txt', 'a') as username:

    while True:
        print("Press 'quit' or 'q' or 'e' to exit")  # inform user that they can quit
        user_name = input("Write your user name: ")  # username prompt

        if user_name.lower() in ['q', 'e', 'quit']:  # condition to quit
            print("You opt to exit")
            print("Goodbye!")
            break

        if user_name in registered_usernames:
            print(f"username {user_name}, Already taken, Please Choose another username.\n")
            continue  # allow user to choose another username.

        print(f"Hello {user_name}, Welcome to my channel")
        username.write(user_name + "\n")

        print(f"{user_name}, Congratulation, you have been added\n")
