#Conditions check: Length of 12 or more, presense of upper and lower case, digits, and symbols.

# Getting password from user input.
password = input("What's the password?\n") 

# Defining minimum password length.
min_length = 12

# One Liner condition that checks for all requirements.

if (len(password) >= min_length) and (password.islower()!= True and password.isupper()!= True) and (password.isalnum()!=True) and (any(char.isdigit() for char in password)):
    print("Your password meets the length, case, digits, and symbols requirements!")
else:
    print("Please try again, your password does not meet the minimum requirements")
        
