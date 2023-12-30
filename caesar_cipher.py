def encrypt(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            # Determine whether the character is uppercase or lowercase
            is_upper = char.isupper()

            # Shift the character by the specified amount
            char_code = ord(char)
            char_code = (char_code - 65 + shift) % 26 + 65 if is_upper else (char_code - 97 + shift) % 26 + 97

            result += chr(char_code)
        else:
            # Preserve non-alphabetic characters
            result += char

    return result


def decrypt(text, shift):
    # Decryption is the same as encryption with a negative shift
    return encrypt(text, -shift)


def main():
    text = input("Enter the text to encrypt/decrypt: ")

    # Prompt the user to enter a shift value
    while True:
        try:
            shift = int(input("Enter the shift value (an integer): "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    encrypted_text = encrypt(text, shift)
    decrypted_text = decrypt(encrypted_text, shift)

    print("\nEncrypted Text:", encrypted_text)
    print("Decrypted Text:", decrypted_text)


if __name__ == "__main__":
    main()
