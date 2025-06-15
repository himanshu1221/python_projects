from cryptography.fernet import Fernet

'''def write_key():
    key = Fernet.generate_key() ## Generate a new key
    with open("key.key", "wb") as key_file: ##open a file in write-binary mode
        key_file.write(key) ## Write the key to a file'''

##write_key() ## Call the function to write the key

def load_key():
    file = open("key.key", "rb") ## Open the key file in read-binary mode
    key = file.read() ## Read the key from the file
    file.close() ## Close the file
    return key ## Return the key

key = load_key() ## Load the key
fer = Fernet(key) ## Create a Fernet object with the key

def view():
    with open("password.txt", "r") as f:
        for line in f.readline():
            data = line.rstrip() ## Remove trailing whitespace
            user, passw = data.split("|") ## Split the line into username and password
            print("User:", user, "| Password:", # Print the username and password "Decrypted password: ",
                fer.decrypt(passw.encode()).decode()) ## Decrypt the password and print it

def add():
    name = input("Account Name: ") ## Get the account name from the user
    pwd = input("Password: ") ## Get the password from the user
    with open("password.txt", "a") as f: ## Open the password file in append mode
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode()+ "\n") ## Encrypt the password and write it to the file

while True:
    mode = input("Would you like to add a new password or view existing ones (view, add), or quit (q)? ").lower() ## Get the mode from the user
    if mode == "q": ## If the user wants to quit
        break ## Exit the loop
    if mode == "view": ## If the user wants to view passwords
        view() ## Call the view function
    elif mode == "add": ## If the user wants to add a password
        add() ## Call the add function
    else: ## If the user entered an invalid option
        print("Invalid option. Please try again.") ## Print an error message
