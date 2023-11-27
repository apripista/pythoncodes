def encrypt_caesar_cipher(plaintext, shift):
    encrypted_text = ""
    for char in plaintext:
        if char.isalpha():
            if char.islower():
                encrypted_char = chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
            else:
                encrypted_char = chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

def main():
    plaintext = input("Enter the plaintext: ")
    shift = int(input("Enter the shift value: "))
    encrypted_text = encrypt_caesar_cipher(plaintext, shift)
    print("Encrypted Text:", encrypted_text)


if __name__ == "__main__":
    main()
