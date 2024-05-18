def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            shift_amount = shift if mode in ['encrypt', 'e'] else -shift
            result += chr((ord(char) - shift_base + shift_amount) % 26 + shift_base)
        elif char.isdigit():
            shift_amount = shift if mode in ['encrypt', 'e'] else -shift
            result += chr((ord(char) - 48 + shift_amount) % 10 + 48)
        else:
            result += char
    return result

def main():
    print("Welcome to the Caesar Cipher Program!")
    mode = input("Do you want to '(E)ncrypt' or '(D)ecrypt' the message? ").strip().lower()
    if mode not in ['encrypt', 'e', 'decrypt', 'd']:
        print("Invalid mode selected. Please choose 'encrypt' or 'decrypt'.")
        return
    
    message = input("Enter the message: ").strip()
    try:
        shift = int(input("Enter the shift value: ").strip())
    except ValueError:
        print("Invalid shift value. Please enter a number.")
        return

    result = caesar_cipher(message, shift, mode)
    print(f"The resulting message is: {result}")

if __name__ == "__main__":
    main()
