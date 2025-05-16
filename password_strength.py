import sys
import re

#password = sys.argv[1]

def passwordvalidation():
    password = input("Enter the password: ")
    if len(password) < 8:
        print("Length of password is too short")
    elif re.search(r"[A-Z]", password) is None:
        print("Pass must contain upper and lower case letters")
    elif re.search(r"[a-z]", password) is None:
        print("Pass must contain upper and lower case letters")
    elif re.search(r"\d", password) is None:
        print("Pass must contain at least one digit")
    elif re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is None:
        print("Pass must contain at least one special character")
    else:
        print("Password is strong")

# Call the function
passwordvalidation()