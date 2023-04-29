import random
import string

def generate_password(length, include_numbers, include_uppercase, include_special):
    '''
    Creates password using constraints given by user
    '''
    characters = string.ascii_lowercase
    if include_numbers:
        characters += string.digits
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_special:
        characters += string.punctuation
    
    password = ''.join(random.choice(characters) for i in range(length))
    
    return password

def main():
    length = int(input("Enter the desired length of the password: "))
    include_numbers = input("Include numbers? (y/n): ").lower() == 'y'
    include_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    include_special = input("Include special characters? (y/n): ").lower() == 'y'
    
    password = generate_password(length, include_numbers, include_uppercase, include_special)
    print("Your generated password is:", password)
    
    
if __name__ == '__main__':
    main()
