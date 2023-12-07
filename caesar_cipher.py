# simple caesar cipher this can be used to encrypt and decrypt a cipher

def decrypt_caesar_cipher(ciphertext, shift):
    decrypted_text = ""
    for char in ciphertext:
        if char.isalpha():
            if char.islower():
                decrypted_char = chr(((ord(char) - ord('a') - shift) % 26) + ord('a'))
            else:
                decrypted_char = chr(((ord(char) - ord('A') - shift) % 26) + ord('A'))
            decrypted_text += decrypted_char
        else:
            decrypted_text += char
    return decrypted_text


def main():
    ciphertext = input("Enter the ciphertext: ")
    shift = int(input("Enter the shift value: "))
    decrypted_text = decrypt_caesar_cipher(ciphertext, shift)
    print("Decrypted Text:", decrypted_text)


if __name__ == "__main__":
    main()
