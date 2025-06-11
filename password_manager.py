from cryptography.fernet import Fernet #module for symmetric encryption

'''
def generate_key():
    key = Fernet.generate_key() # Generate a key for encryption
    ##print(key) # Print the key in a readable format
    with open("key.key", "wb") as key_file:
        key_file.write(key)
        # .key is a file that stores the encryption key
        # Open a file to write the key
        # "wb" mode to write the key in binary format
        #key.key is a file that stores the encryption key
        
generate_key() # Call the function to generate the key'''

def load_key():
    file =  open("key.key", "rb") #rb mode to read the key in binary format
    key = file.read() # Read the key from the file
    file.close() # Close the file after reading
    return key # Return the key for encryption/decryption


mstr_pwd = input("Enter your master password: ")
key = load_key() + mstr_pwd.encode() # Load the key from the file
fernet = Fernet(key) # Create a Fernet object with the key
mode = input("Enter 'add' to add a new password or 'get' to retrieve a password: ").lower()

def get():
    print("Retrieving a password...")
    with open("passwords.txt", "r") as f:
        for line in f.readlines():
            data =  line.rstrip() #rstrip Remove trailing newline characters
            usr_name, pwd = data.split(":") # Split the line into username and password
            print(f"Username: {usr_name}, Password: {fernet.decrypt(pwd.encode()).decode()}") # Decrypt the password and print it
            #fernet.decrypt() to decrypt the password
    exit()

def new():
    print("Adding a new password...")
    usr_name = input("Enter the username: ")
    pwd = input("Enter the password: ")
    with open("passwords.txt","a") as f: #"a" mode to append to the file #with statement to ensure the file is closed after writing
        f.write(f"{usr_name}:{fernet.encrypt(pwd.encode().decode())}\n")
        #fernet.encrypt() to encrypt the password
        #pwd.encode() to convert the password to bytes
        #f.write() to write the username and encrypted password to the file
    print("Password added successfully.")
    exit()

while True:
    if mode != 'add' and mode != 'get':
        print("Invalid mode. Please enter 'add' or 'get'.")
        mode = input("Enter 'add' to add a new password or 'get' to retrieve a password: ").lower()
        continue
    if mode == 'add':
        new()
    elif mode == 'get':
        get()