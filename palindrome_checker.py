def is_palindrome(input_str):
    # Remove spaces and convert to lowercase (for words)
    clean_str = ''.join(input_str.split()).lower()

    # Compare with its reverse
    return clean_str == clean_str[::-1]


def main():
    user_input = input("Enter a word or number: ")

    if is_palindrome(user_input):
        print("It's a palindrome!")
    else:
        print("It's not a palindrome.")


if __name__ == "__main__":
    main()
