def encode(password):
# Antonio Taveras, Lab 6 - Group 50 
    encoded = ""
    for num in str(password):
        new_num = int(num) + 3
        encoded += str(new_num)
    return encoded

def decode():
    pass

def menu():
    print("""Menu
-------------
1. Encode
2. Decode
3. Quit""")
    
def main():
    while True:
        menu()
        option = int(input("Please enter an option: "))
        if option == 1:
            password = input("Please enter your password to encode: ")
            encoded = encode(password)
            print("Your password has been encoded and stored!\n")
        elif option == 2:
            decoded = decode(encoded)
            print(f"The encoded password is {encoded}, and the original password is {decoded}.\n")
        elif option == 3:
            break
    
if __name__ == "__main__":
    main()