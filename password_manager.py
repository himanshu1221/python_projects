mstr_pwd = input("Enter your master password: ")

mode = input("Enter 'add' to add a new password or 'get' to retrieve a password: ").lower()

def get():
    print("Retrieving a password...")
    with open("passwords.txt", "r") as f:
        for line in f.readlines():
            data =  line.rstrip() #rstrip Remove trailing newline characters
            usr_name, pwd = data.split(":") # Split the line into username and password
            print(f"Username: {usr_name}, Password: {pwd}")
    exit()

def new():
    print("Adding a new password...")
    usr_name = input("Enter the username: ")
    pwd = input("Enter the password: ")
    with open("passwords.txt","a") as f: #"a" mode to append to the file
        f.write(f"{usr_name}:{pwd}\n")
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
    

    